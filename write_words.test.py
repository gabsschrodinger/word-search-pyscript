import unittest
from letter_grid import generate_random_letter_grid
from write_words import write_word_horizontally, write_word_vertically
from tracked_words import written_words, clean_up_words
import random


class TestHorizontalWords(unittest.TestCase):
    def setUp(self):
        clean_up_words()

    def test_write_word(self):
        test_string = "TEST"
        letter_grid = generate_random_letter_grid(10, 10)
        grid_y = random.randint(0, len(letter_grid) - 1)
        grid_x = random.randint(0, len(letter_grid[0]) - 1 - len(test_string))

        letter_grid = write_word_horizontally(
            letter_grid, test_string, grid_x, grid_y)

        for letter in test_string:
            self.assertEqual(letter_grid[grid_y]
                             [grid_x]["value"], letter.upper())
            grid_x += 1

    def test_locked_letter(self):
        test_string = "TEST"
        exception_string = "EXCEPTION"
        letter_grid = generate_random_letter_grid(10, 10)
        grid_y = random.randint(0, len(letter_grid) - 1)
        grid_x = random.randint(0, len(letter_grid[0]) - 1 - len(test_string))

        letter_grid = write_word_horizontally(
            letter_grid, test_string, grid_x, grid_y)

        self.assertRaises(Exception, write_word_horizontally,
                          letter_grid, exception_string, None, grid_y)

    def test_tracking_word(self):
        test_string = "TEST"
        letter_grid = generate_random_letter_grid(10, 10)
        grid_y = random.randint(0, len(letter_grid) - 1)
        grid_x = random.randint(0, len(letter_grid[0]) - 1 - len(test_string))

        letter_grid = write_word_horizontally(
            letter_grid, test_string, grid_x, grid_y)

        self.assertIn(test_string, map(lambda x: x["word"], written_words))

        coordinate_list = list(map(lambda x: (x, grid_y), range(
            grid_x, grid_x + len(test_string))))
        tracked_coordinates = list(filter(lambda x: x["word"] == test_string, written_words))[0]["coordinates"]
        self.assertListEqual(coordinate_list, tracked_coordinates)


class TestVerticalWords(unittest.TestCase):
    def setUp(self):
        clean_up_words()

    def test_write_word(self):
        test_string = "TEST"
        letter_grid = generate_random_letter_grid(10, 10)
        grid_y = random.randint(0, len(letter_grid) - 1 - len(test_string))
        grid_x = random.randint(0, len(letter_grid[0]) - 1)

        letter_grid = write_word_vertically(
            letter_grid, test_string, grid_x, grid_y)

        for letter in test_string:
            self.assertEqual(letter_grid[grid_y]
                             [grid_x]["value"], letter.upper())
            grid_y += 1

    def test_locked_letter(self):
        test_string = "TEST"
        exception_string = "EXCEPTION"
        letter_grid = generate_random_letter_grid(10, 10)
        grid_y = random.randint(0, len(letter_grid) - 1 - len(test_string))
        grid_x = random.randint(0, len(letter_grid[0]) - 1)

        letter_grid = write_word_vertically(
            letter_grid, test_string, grid_x, grid_y)

        self.assertRaises(Exception, write_word_vertically,
                          letter_grid, exception_string, grid_x, None)
        
    def test_tracking_word(self):
        test_string = "TEST"
        letter_grid = generate_random_letter_grid(10, 10)
        grid_y = random.randint(0, len(letter_grid) - 1 - len(test_string))
        grid_x = random.randint(0, len(letter_grid[0]) - 1)

        letter_grid = write_word_vertically(
            letter_grid, test_string, grid_x, grid_y)

        self.assertIn(test_string, map(lambda x: x["word"], written_words))

        coordinate_list = list(map(lambda y: (grid_x, y), range(
            grid_y, grid_y + len(test_string))))
        tracked_coordinates = list(filter(lambda x: x["word"] == test_string, written_words))[0]["coordinates"]
        self.assertListEqual(coordinate_list, tracked_coordinates)


unittest.main()
