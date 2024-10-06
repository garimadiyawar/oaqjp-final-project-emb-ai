from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        r1=emotion_detector('I am glad this happened')
        self.assertEqual(r1['dominant_emotion'], 'joy')

        r2=emotion_detector('I am really mad about this')
        self.assertEqual(r2['dominant_emotion'], 'anger')

        r3=emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(r3['dominant_emotion'], 'disgust')

        r4=emotion_detector('I am so sad about this')
        self.assertEqual(r4['dominant_emotion'], 'sadness')

        r5=emotion_detector('I am really afraid that this will happen')
        self.assertEqual(r5['dominant_emotion'], 'fear')

unittest.main()