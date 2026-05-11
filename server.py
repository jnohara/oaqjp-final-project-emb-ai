from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return jsonify({"error": "Bad Request", "message": "No text provided."}), 400
    result = emotion_detector(text_to_analyze)
    return jsonify(result)

@app.route("/")
def home():
    return "Welcome to Emotion Detection API"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
