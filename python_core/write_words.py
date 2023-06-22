import random
from python_core.tracked_words import written_words, randomize_coordinates
from python_core.letter_grid import letter_grid
from typing import Callable


def write_word_generic(word: str, width: int, height: int, update_coordinates_callback: Callable[[(int, int)], tuple], render_board_callback: Callable[[], None]) -> None:
    x_coordinate = width
    y_coordinate = height

    coordinates = []
    for letter in word:
        if letter_grid[y_coordinate][x_coordinate]["locked"] > 0 and letter_grid[y_coordinate][x_coordinate]["value"] != letter:
            randomize_coordinates(coordinates, render_board_callback)
            raise Exception("Letter is locked")

        entry = {
            "value": letter,
            "locked": letter_grid[y_coordinate][x_coordinate]["locked"] + 1,
            "coordinate": (x_coordinate, y_coordinate)
        }
        letter_grid[y_coordinate][x_coordinate] = entry
        coordinates.append((x_coordinate, y_coordinate))

        (x_coordinate, y_coordinate) = update_coordinates_callback(
            (x_coordinate, y_coordinate))

    tracked_word = {
        "word": word,
        "coordinates": coordinates
    }

    written_words.append(tracked_word)


def write_word_horizontally(word: str, render_words_callback: Callable[[], None], render_board_callback: Callable[[], None]) -> None:
    height = random.randint(0, len(letter_grid) - 1)
    width = random.randint(0, len(letter_grid[0]) - len(word))

    write_word_generic(word, width, height, lambda x: (
        x[0] + 1, x[1]), render_board_callback)

    render_words_callback()


def write_word_vertically(word: str, render_words_callback: Callable[[], None], render_board_callback: Callable[[], None]) -> None:
    height = random.randint(0, len(letter_grid) - len(word))
    width = random.randint(0, len(letter_grid[0]) - 1)

    write_word_generic(word, width, height, lambda x: (
        x[0], x[1] + 1), render_board_callback)

    render_words_callback()


def write_word_forward_diagonal(word: str, render_words_callback: Callable[[], None], render_board_callback: Callable[[], None]) -> None:
    height = random.randint(0, len(letter_grid) - len(word))
    width = random.randint(0, len(letter_grid[0]) - len(word))

    write_word_generic(word, width, height, lambda x: (
        x[0] + 1, x[1] + 1), render_board_callback)

    render_words_callback()


def randomly_write_word(word: str, render_words_callback: Callable[[], None], render_board_callback: Callable[[], None]) -> None:
    random_option = random.randint(1, 3)

    match random_option:
        case 1:
            write_word_horizontally(
                word.upper(), render_words_callback, render_board_callback)
        case 2:
            write_word_vertically(
                word.upper(), render_words_callback, render_board_callback)
        case 3:
            write_word_forward_diagonal(
                word.upper(), render_words_callback, render_board_callback)


def write_with_retry(word: str, render_words_callback: Callable[[], None], render_board_callback: Callable[[], None]) -> None:
    attempts = 0

    while attempts < 1000:
        try:
            randomly_write_word(word, render_words_callback,
                                render_board_callback)

            return
        except:
            attempts += 1

    raise Exception("Too many attempts. Cannot add word :(")
