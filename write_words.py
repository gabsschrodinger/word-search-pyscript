import random
from typing import List


def write_word_horizontally(letter_grid: List[str], word: str, grid_x: int = None, grid_y: int = None) -> List[str]:
    new_grid = letter_grid.copy()

    height = random.randint(
        0, len(letter_grid) - 1) if grid_y == None else grid_y
    starting_index = random.randint(
        0, len(letter_grid[0]) - 1 - len(word)) if grid_x == None else grid_x

    for letter in word:
        new_grid[height][starting_index] = letter
        starting_index += 1

    return new_grid
