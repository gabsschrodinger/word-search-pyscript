import unittest
from letter_grid import generate_random_letter_grid
from write_words import write_word_horizontally
import random


class TestHorizontalWords(unittest.TestCase):

    def test_write_word(self):
        test_string = "TEST"
        letter_grid = generate_random_letter_grid(10, 10)
        grid_y = random.randint(0, len(letter_grid) - 1)
        grid_x = random.randint(0, len(letter_grid[0]) - 1 - len(test_string))

        letter_grid = write_word_horizontally(
            letter_grid, test_string, grid_x, grid_y)

        for letter in test_string:
            self.assertEqual(letter_grid[grid_y][grid_x], letter.upper())
            grid_x += 1


unittest.main()
