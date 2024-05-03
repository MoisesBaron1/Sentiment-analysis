from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        result_3 = sentiment_analyzer('I am neutral working with Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')
        result_4 = sentiment_analyzer('Amo trabajar con python')
        self.assertEqual(result_4['label'], 'SENT_POSITIVE')
        result_5 = sentiment_analyzer('Odio trabajar con python')
        self.assertEqual(result_5['label'], 'SENT_NEGATIVE')
        result_6 = sentiment_analyzer('Es neutral trabajar con python')
        self.assertEqual(result_6['label'], 'SENT_NEUTRAL')

unittest.main()