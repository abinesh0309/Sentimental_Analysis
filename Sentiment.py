import curses
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(review):
    sentiment = analyzer.polarity_scores(review)
    compound_score = sentiment['compound']
    
    if compound_score >= 0.05:
        sentiment_result = "Positive"
    elif compound_score <= -0.05:
        sentiment_result = "Negative"
    else:
        sentiment_result = "Neutral"
    
    return sentiment_result, compound_score

# Main function for the terminal-based GUI
def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # Set up some initial instructions
    stdscr.addstr(0, 0, "Product Review Sentiment Analysis System")
    stdscr.addstr(1, 0, "--------------------------------------------------")
    stdscr.addstr(3, 0, "Please enter a product review and press Enter.")
    stdscr.addstr(4, 0, "Type 'exit' to quit the program.")
    
    stdscr.addstr(6, 0, "Your Review: ")

    # Create a blank string to hold the review input
    review = ""
    while True:
        stdscr.addstr(7, 0, review)
        stdscr.refresh()

        # Capture the user's input
        char = stdscr.getch()
        
        # If user presses Enter, perform analysis
        if char == 10:  # Enter key
            if review.lower() == 'exit':
                break

            sentiment_result, score = analyze_sentiment(review)

            # Display the sentiment analysis results
            stdscr.clear()
            stdscr.addstr(0, 0, "Product Review Sentiment Analysis System")
            stdscr.addstr(1, 0, "--------------------------------------------------")
            stdscr.addstr(3, 0, f"Review: {review}")
            stdscr.addstr(4, 0, f"Sentiment: {sentiment_result}")
            stdscr.addstr(5, 0, f"Sentiment Score: {score:.2f}")
            stdscr.addstr(6, 0, "\nPress any key to continue...")

            # Wait for a key press before going back to review input
            stdscr.getch()
            stdscr.clear()
            stdscr.addstr(6, 0, "Your Review: ")
            review = ""
        
        # If the user presses the backspace key, remove the last character
        elif char == 127:  # Backspace key
            review = review[:-1]
        else:
            # Append the character to the review string
            review += chr(char)

# Run the curses application
curses.wrapper(main)