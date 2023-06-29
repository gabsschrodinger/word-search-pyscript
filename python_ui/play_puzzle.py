from js import window, document
from typing import TypedDict, List
from python_core.letter_grid import LetterCell
from python_core.tracked_words import WrittenWord
from urllib import parse
from python_core.encode_utils import decode_data


class PuzzleConfig(TypedDict):
    words: List[WrittenWord]
    letter_grid: List[List[LetterCell]]


raw_puzzle_config = str(window.location).split("play.html?game=", 1)[1]

puzzle_config: PuzzleConfig = decode_data(raw_puzzle_config)

letter_grid = puzzle_config["letter_grid"]
# print(str(window.location).split("play.html?game=", 1)[1])
# print(decode_data(str(window.location).split("play.html?game=", 1)[1]))


def render_board():
    game_board = document.querySelector(".game-board")
    game_board.replaceChildren()

    for i in range(len(letter_grid)):
        current_row = document.createElement("div")
        current_row.setAttribute("class", "letter-grid-row")
        for j in letter_grid[i]:
            letter_div = document.createElement("div")
            letter_div.setAttribute("class", "game-letter-div")
            letter_div.classList.add("coordinate-" +
                                     str(j["coordinate"][0]) + "-" + str(j["coordinate"][1]))
            letter_div_content = document.createTextNode(j["value"])
            letter_div.appendChild(letter_div_content)
            current_row.appendChild(letter_div)
        game_board.appendChild(current_row)

render_board()