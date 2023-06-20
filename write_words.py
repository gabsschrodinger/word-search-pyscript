import random
from tracked_words import written_words, randomize_coordinates
from letter_grid import letter_grid
from typing import Callable


def write_word_horizontally(word: str, render_words_callback: Callable[[], None], render_board_callback: Callable[[], None]) -> None:
    height = random.randint(0, len(letter_grid) - 1)
    starting_width = random.randint(0, len(letter_grid[0]) - len(word))

    coordinates = []
    for letter in word:
        if letter_grid[height][starting_width]["locked"] > 0 and letter_grid[height][starting_width]["value"] != letter:
            randomize_coordinates(coordinates, render_board_callback)
            raise Exception("Letter is locked")

        entry = {
            "value": letter,
            "locked": letter_grid[height][starting_width]["locked"] + 1
        }
        letter_grid[height][starting_width] = entry
        coordinates.append((starting_width, height))
        starting_width += 1

    tracked_word = {
        "word": word,
        "coordinates": coordinates
    }

    written_words.append(tracked_word)

    render_words_callback()


def write_word_vertically(word: str, render_words_callback: Callable[[], None], render_board_callback: Callable[[], None]) -> None:
    starting_height = random.randint(0, len(letter_grid) - len(word))
    width = random.randint(0, len(letter_grid[0]) - 1)

    coordinates = []
    for letter in word:
        if letter_grid[starting_height][width]["locked"] > 0 and letter_grid[starting_height][width]["value"] != letter:
            randomize_coordinates(coordinates, render_board_callback)
            raise Exception("Letter is locked")

        entry = {
            "value": letter,
            "locked": letter_grid[starting_height][width]["locked"] + 1
        }
        letter_grid[starting_height][width] = entry
        coordinates.append((width, starting_height))
        starting_height += 1

    tracked_word = {
        "word": word,
        "coordinates": coordinates
    }

    written_words.append(tracked_word)

    render_words_callback()


def randomly_write_word(word: str, render_words_callback: Callable[[], None], render_board_callback: Callable[[], None]) -> None:
    random_option = random.randint(1, 2)

    match random_option:
        case 1:
            write_word_horizontally(
                word.upper(), render_words_callback, render_board_callback)
        case 2:
            write_word_vertically(
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
