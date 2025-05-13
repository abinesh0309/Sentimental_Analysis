import os
import docx2txt
import PyPDF2
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

console = Console()

# ----------- Helper Functions -----------

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return " ".join([page.extract_text() or "" for page in reader.pages])
    except:
        return ""

def extract_text_from_docx(file_path):
    try:
        return docx2txt.process(file_path)
    except:
        return ""

def load_resumes(folder_path):
    resumes = []
    for file in os.listdir(folder_path):
        if file.endswith('.pdf') or file.endswith('.docx'):
            path = os.path.join(folder_path, file)
            text = extract_text_from_pdf(path) if file.endswith('.pdf') else extract_text_from_docx(path)
            if text.strip():
                resumes.append((file, text))
    return resumes

def rank_resumes(resumes, jd_text):
    documents = [jd_text] + [text for _, text in resumes]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    ranked = sorted(zip([name for name, _ in resumes], cosine_similarities), key=lambda x: x[1], reverse=True)
    return [(name, round(score * 100, 2)) for name, score in ranked]

# ----------- Main Execution -----------

if __name__ == "__main__":
    resume_folder = "resumes"
    jd_path = "jd.txt"

    if not os.path.exists(resume_folder):
        console.print(f"[red]❌ Folder '{resume_folder}' not found. Please create it and add resumes.[/red]")
        exit()

    if not os.path.isfile(jd_path):
        console.print(f"[red]❌ Job description file '{jd_path}' not found.[/red]")
        exit()

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        progress.add_task(description="Loading resumes...", total=None)
        resumes = load_resumes(resume_folder)

    if not resumes:
        console.print("[yellow]⚠️ No valid resumes found in the folder.[/yellow]")
        exit()

    with open(jd_path, "r", encoding="utf-8") as f:
        jd_text = f.read()

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        progress.add_task(description="Ranking resumes...", total=None)
        ranked_resumes = rank_resumes(resumes, jd_text)

    table = Table(title="📊 Resume Match Results")
    table.add_column("Resume", style="cyan")
    table.add_column("Match (%)", justify="right", style="green")

    for name, score in ranked_resumes:
        table.add_row(name, f"{score}%")

    console.print(table)

    df = pd.DataFrame(ranked_resumes, columns=["Resume", "Match (%)"])
    df.to_csv("results.csv", index=False)
    console.print("\n[bold green]✅ Results saved to [underline]results.csv[/underline][/bold green]")
