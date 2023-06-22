import unittest
import random
from python_core.letter_grid import generate_random_letter_grid

class TestHorizontalWords(unittest.TestCase):

    def test_grid_is_list(self):
        random_height = random.randint(0, 100)
        random_length = random.randint(0, 100)

        generated_grid = generate_random_letter_grid(random_length, random_height)
        self.assertEqual(type(generated_grid), type([]))

    def test_grid_items_are_lists(self):
        random_height = random.randint(0, 100)
        random_length = random.randint(0, 100)

        generated_grid = generate_random_letter_grid(random_length, random_height)
        for item in generated_grid:
            self.assertEqual(type(item), type([]))

    def test_grid_subitems_are_objects(self):
        random_height = random.randint(0, 100)
        random_length = random.randint(0, 100)

        generated_grid = generate_random_letter_grid(random_length, random_height)
        for item in generated_grid:
            for subitem in item:
                self.assertEqual(type(subitem["value"]), type(""))
                self.assertEqual(subitem["locked"], False)

unittest.main()