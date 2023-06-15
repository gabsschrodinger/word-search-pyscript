import random
import string
from typing import List


def generate_random_letter_grid(grid_length: int, grid_height: int) -> List[List[dict]]:
    letter_grid = []

    for height_index in range(grid_height):
        current_row = []
        for length_index in range(grid_length):
            entry = {
                'value': random.choice(string.ascii_letters).upper(),
                'locked': False
            }
            current_row.append(entry)
        letter_grid.append(current_row)

    return letter_grid
