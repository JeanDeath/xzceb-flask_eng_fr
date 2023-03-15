import unittest

from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(None), "")
        self.assertEqual(english_to_french(""), "")


    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Bonjour mon ami"), "Hello my friend")
        self.assertEqual(french_to_english(None), "")
        self.assertEqual(french_to_english(""), "")

if __name__=='__main__':
    unittest.main()