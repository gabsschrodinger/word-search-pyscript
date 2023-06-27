import random
from python_core.tracked_words import written_words, randomize_coordinates
from python_core.letter_grid import letter_grid
from typing import Callable


def write_word_generic(word: str, width: int, height: int, update_coordinates: Callable[[(int, int)], tuple], mode: str) -> None:
    x_coordinate = width
    y_coordinate = height

    coordinates = []
    for letter in word:
        if letter_grid[y_coordinate][x_coordinate]["locked"] > 0 and letter_grid[y_coordinate][x_coordinate]["value"] != letter:
            randomize_coordinates(coordinates)
            raise Exception("Letter is locked")

        entry = {
            "value": letter,
            "locked": letter_grid[y_coordinate][x_coordinate]["locked"] + 1,
            "coordinate": (x_coordinate, y_coordinate)
        }
        letter_grid[y_coordinate][x_coordinate] = entry
        coordinates.append((x_coordinate, y_coordinate))

        (x_coordinate, y_coordinate) = update_coordinates(
            (x_coordinate, y_coordinate))

    if mode == "ADD":
        tracked_word = {
            "word": word,
            "coordinates": coordinates
        }

        written_words.append(tracked_word)
    elif mode == "UPDATE":
        written_word = next(filter(lambda x: x["word"] == word, written_words))
        written_word["coordinates"] = coordinates


def write_word_horizontally(word: str, mode: str) -> None:
    height = random.randint(0, len(letter_grid) - 1)
    width = random.randint(0, len(letter_grid[0]) - len(word))

    write_word_generic(word, width, height, lambda x: (
        x[0] + 1, x[1]), mode)



def write_word_vertically(word: str, mode: str) -> None:
    height = random.randint(0, len(letter_grid) - len(word))
    width = random.randint(0, len(letter_grid[0]) - 1)

    write_word_generic(word, width, height, lambda x: (
        x[0], x[1] + 1), mode)


def write_word_forward_diagonal(word: str, mode: str) -> None:
    height = random.randint(0, len(letter_grid) - len(word))
    width = random.randint(0, len(letter_grid[0]) - len(word))

    write_word_generic(word, width, height, lambda x: (
        x[0] + 1, x[1] + 1), mode)


def randomly_write_word(word: str, mode: str) -> None:
    random_option = random.randint(1, 3)

    match random_option:
        case 1:
            write_word_horizontally(word.upper(), mode)
        case 2:
            write_word_vertically(word.upper(), mode)
        case 3:
            write_word_forward_diagonal(word.upper(), mode)


def write_with_retry(word: str, mode: str = "ADD") -> None:
    if len(word) > len(letter_grid) and len(word) > len(letter_grid[0]):
        raise Exception("It's not possible to add a word longer than the board length/height.")

    attempts = 0

    while attempts < 1000:
        try:
            randomly_write_word(word, mode)

            return
        except:
            attempts += 1

    raise Exception("Too many attempts. Try increasing the size of the board or removing word before adding more words.")


def rewrite_word(word: str) -> None:
    written_word = next(filter(lambda x: x["word"] == word, written_words))
    randomize_coordinates(written_word["coordinates"])
    write_with_retry(word, "UPDATE")
