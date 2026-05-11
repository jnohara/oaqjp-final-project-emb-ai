from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_analyzer():
    try:
        text_to_analyze = request.args.get('textToAnalyze')
        
        # Validar que haya texto
        if not text_to_analyze:
            return jsonify({
                'error': 'Bad Request',
                'message': 'No text provided. Please use ?textToAnalyze=YOUR_TEXT'
            }), 400
        
        # Validar que no esté vacío
        if not text_to_analyze.strip():
            return jsonify({
                'error': 'Bad Request',
                'message': 'Text cannot be empty'
            }), 400
        
        # Analizar emociones
        result = emotion_detector(text_to_analyze)
        
        # Verificar si hubo error en el análisis
        if result.get('error'):
            return jsonify({
                'error': 'Internal Server Error',
                'message': 'Failed to analyze emotion'
            }), 500
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred'
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
        'message': 'Endpoint not found'
    }), 404

@app.route('/')
def home():
    return "Welcome to the Emotion Detection API! Use /emotionDetector?textToAnalyze=YOUR_TEXT"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)