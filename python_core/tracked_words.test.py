import unittest
from python_core.tracked_words import written_words, clean_up_words

class TestHorizontalWords(unittest.TestCase):
    def test_clean_up(self):
        test_string = "TEST"
        coordinates = [(0, 1), (0, 2), (0, 3)]
        entry = {
            "word": test_string,
            "coordinates": coordinates
        }
        written_words.append(entry)
        clean_up_words()

        self.assertListEqual(written_words, [])
        
unittest.main()