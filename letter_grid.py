import random
import string
from typing import List

def generate_random_letter_grid(grid_length: int, grid_height: int) -> List[str]:
    letter_grid = []

    for height_index in range(grid_height):
        current_row = []
        for length_index in range(grid_length):
            current_row.append(random.choice(string.ascii_letters).upper())
        letter_grid.append(current_row)

    return letter_grid