"""
Server application for emotion detection using Flask.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create a Flask app instance
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect emotion from a given text.
    This function extracts text from the query parameter and
    returns the emotion detection results.

    Returns:
        str: Formatted emotion detection result or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None (error case)
    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again."

    # Return formatted emotion detection result
    return (f"For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}.")


@app.route("/")
def render_index_page():
    """
    Render the index page.
    
    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 with port 5000
    app.run(host="0.0.0.0", port=5000)
