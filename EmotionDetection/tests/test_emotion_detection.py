import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy_detection(self):
        result = emotion_detector("I am very happy and excited!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_detection(self):
        result = emotion_detector("I am so angry and frustrated!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness_detection(self):
        result = emotion_detector("I feel very sad and depressed.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_detection(self):
        result = emotion_detector("I am scared and terrified.")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_null_input(self):
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()