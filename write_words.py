import random
from typing import List

written_words = []


def write_word_horizontally(letter_grid: List[List[dict]], word: str, grid_x: int = None, grid_y: int = None) -> List[List[dict]]:
    new_grid = letter_grid.copy()

    height = random.randint(
        0, len(letter_grid) - 1) if grid_y == None else grid_y
    starting_width = random.randint(
        0, len(letter_grid[0]) - 1 - len(word)) if grid_x == None else grid_x

    for letter in word:
        if new_grid[height][starting_width]["locked"] and new_grid[height][starting_width]["value"] != letter:
            raise Exception("Letter is locked")

        entry = {
            "value": letter,
            "locked": True
        }
        new_grid[height][starting_width] = entry
        starting_width += 1

    return new_grid

def write_word_vertically(letter_grid: List[List[dict]], word: str, grid_x: int = None, grid_y: int = None) -> List[List[dict]]:
    new_grid = letter_grid.copy()

    starting_height = random.randint(
        0, len(letter_grid) - 1 - len(word)) if grid_y == None else grid_y
    width = random.randint(
        0, len(letter_grid[0]) - 1) if grid_x == None else grid_x

    for letter in word:
        if new_grid[starting_height][width]["locked"] and new_grid[starting_height][width]["value"] != letter:
            raise Exception("Letter is locked")

        entry = {
            "value": letter,
            "locked": True
        }
        new_grid[starting_height][width] = entry
        starting_height += 1

    return new_grid