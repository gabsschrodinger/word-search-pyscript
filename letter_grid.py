import random
import string
from typing import List, TypedDict

class LetterCell(TypedDict):
    value: str
    locked: int

def generate_random_letter_grid(grid_length: int, grid_height: int) -> List[List[LetterCell]]:
    letter_grid: List[List[LetterCell]] = []

    for height_index in range(grid_height):
        current_row: List[LetterCell] = []
        for length_index in range(grid_length):
            entry: LetterCell = {
                'value': random.choice(string.ascii_letters).upper(),
                'locked': 0
            }
            current_row.append(entry)
        letter_grid.append(current_row)

    return letter_grid


letter_grid = generate_random_letter_grid(15, 15)
