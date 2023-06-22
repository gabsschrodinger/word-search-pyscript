from typing import List, TypedDict
from python_core.letter_grid import letter_grid
import random
import string


class WrittenWord(TypedDict):
    word: str
    coordinates: List[tuple]


written_words: List[WrittenWord] = []


def clean_up_words() -> None:
    written_words.clear()


def randomize_coordinates(coordinates: List[tuple]) -> None:
    for coordinate in coordinates:
        entry = {
            "value": random.choice(string.ascii_letters).upper() if letter_grid[coordinate[1]][coordinate[0]]["locked"] <= 1 else letter_grid[coordinate[1]][coordinate[0]]["value"],
            "locked": letter_grid[coordinate[1]][coordinate[0]]["locked"] - 1,
            "coordinate": (coordinate[0], coordinate[1])
        }
        letter_grid[coordinate[1]][coordinate[0]] = entry


def remove_word(word: str) -> None:
    word_to_remove = next(
        filter(lambda x: x["word"] == word, written_words))
    coordinates = word_to_remove["coordinates"]

    randomize_coordinates(coordinates)

    written_words.remove(word_to_remove)
