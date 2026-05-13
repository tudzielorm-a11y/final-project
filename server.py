from flask import Flask, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_analyzer():

    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None (indicating a 400 error)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Otherwise, return the successful formatted string
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

# MOVED TO THE LEFT - This must be outside the function!
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)