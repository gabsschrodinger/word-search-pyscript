from js import document
from typing import List
from letter_grid import letter_grid
import random
import string
from board import rerender_board
from pyodide.ffi.wrappers import add_event_listener

written_words: List[dict] = []


def clean_up_words() -> None:
    written_words.clear()


def randomize_coordinates(coordinates: List[tuple]) -> None:
    for coordinate in coordinates:
        entry = {
            "value": random.choice(string.ascii_letters).upper() if letter_grid[coordinate[1]][coordinate[0]]["locked"] <= 1 else letter_grid[coordinate[1]][coordinate[0]]["word"],
            "locked": letter_grid[coordinate[1]][coordinate[0]]["locked"] - 1
        }
        letter_grid[coordinate[1]][coordinate[0]] = entry

    rerender_board()


def remove_word(word: str) -> None:
    word_to_remove = list(
        filter(lambda x: x["word"] == word, written_words))[0]
    coordinates = word_to_remove["coordinates"]

    randomize_coordinates(coordinates)

    written_words.pop(written_words.index(word_to_remove))
    display_tracked_words()


def display_tracked_words() -> None:
    written_words_div = document.querySelector(".written-words")
    written_words_div.replaceChildren()

    for word in written_words:
        new_word = document.createElement("div")
        new_word.setAttribute("class", "written-word")
        new_word_content = document.createTextNode(word["word"])
        new_word.appendChild(new_word_content)

        new_word_remove_btn = document.createElement("div")
        new_word_remove_btn.setAttribute("class", "written-word-remove-btn")
        remove_word_content = document.createTextNode("X")
        new_word_remove_btn.appendChild(remove_word_content)

        add_event_listener(new_word_remove_btn, "click",
                           lambda _: remove_word(word["word"]))

        new_word.appendChild(new_word_remove_btn)

        written_words_div.appendChild(new_word)
