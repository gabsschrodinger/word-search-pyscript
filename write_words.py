import random
from tracked_words import written_words, display_tracked_words, randomize_coordinates
from letter_grid import letter_grid


def write_word_horizontally(word: str, grid_x: int = None, grid_y: int = None) -> None:
    height = random.randint(
        0, len(letter_grid) - 1) if grid_y == None else grid_y
    starting_width = random.randint(
        0, len(letter_grid[0]) - len(word)) if grid_x == None else grid_x

    coordinates = []
    for letter in word:
        if letter_grid[height][starting_width]["locked"] > 0 and letter_grid[height][starting_width]["value"] != letter:
            randomize_coordinates(coordinates)
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

    display_tracked_words()


def write_word_vertically(word: str, grid_x: int = None, grid_y: int = None) -> None:
    starting_height = random.randint(
        0, len(letter_grid) - len(word)) if grid_y == None else grid_y
    width = random.randint(
        0, len(letter_grid[0]) - 1) if grid_x == None else grid_x

    coordinates = []
    for letter in word:
        if letter_grid[starting_height][width]["locked"] > 0 and letter_grid[starting_height][width]["value"] != letter:
            randomize_coordinates(coordinates)
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

    display_tracked_words()


def randomly_write_word(word: str) -> None:
    random_option = random.randint(1, 2)

    match random_option:
        case 1:
            write_word_horizontally(word.upper())
        case 2:
            write_word_vertically(word.upper())

def write_with_retry(word:str) -> None:
    attempts = 0

    while attempts < 1000:
        try:
            randomly_write_word(word)

            return
        except:
            attempts += 1

    raise Exception("Too many attempts. Cannot add word :(")