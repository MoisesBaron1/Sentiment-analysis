"""
Module for sentiment analysis application.
This module contains the Flask application for a sentiment analysis service.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Perform sentiment analysis on text received from the HTML interface.
    The output returned shows the label and its confidence score for the provided text.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyse)
    label = response['label']
    score = response['score']
    if label is None:
        return "Invalid input ! Try again."
    return (
        f"The given text has been identified as {label.split('_')[1]} "
        f"with a score of {score}."
    )

@app.route("/")
def render_index_page():
    """
    Initiate the rendering of the main application page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
