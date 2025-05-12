# Sentimental_Analysis
NM project
📦 Product Review Sentiment Analysis System
A terminal-based sentiment analysis tool that analyzes user-written product reviews and classifies them as Positive, Negative, or Neutral using VADER (Valence Aware Dictionary and sEntiment Reasoner).

✅ Features
Interactive terminal UI using the curses library.

Real-time sentiment classification (Positive, Negative, Neutral).

Compound sentiment score display.

Option to exit anytime with "exit" command.

Backspace support and input validation.

🛠️ Requirements
Python 3.6+

vaderSentiment library

📥 Installation
Clone this repository or copy the script.

Install dependencies:

bash
Copy
Edit
pip install vaderSentiment
▶️ How to Run
Run the script using Python:

bash
Copy
Edit
python sentiment_terminal.py
🖥️ Usage
Type your product review at the prompt.

Press Enter to analyze the sentiment.

View the result with sentiment type and compound score.

Press any key to return to input.

Type exit to quit the program.

🧠 Example
yaml
Copy
Edit
Your Review: This product works great and exceeded my expectations!

Sentiment: Positive
Sentiment Score: 0.82
📚 Libraries Used
curses – for building terminal-based GUI

vaderSentiment – for sentiment analysis

📝 Notes
This program runs in the terminal, so ensure your terminal supports curses (Windows users may need to run through WSL or use compatible terminals like Git Bash or PowerShell 7+).

Unicode or special characters are not supported in input.

