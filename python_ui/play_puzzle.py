from js import window
from typing import TypedDict, List
from python_core.letter_grid import LetterCell
from python_core.tracked_words import WrittenWord
from urllib import parse
from python_core.encode_utils import decode_data

class RawPuzzleConfig(TypedDict):
    game: str

class PuzzleConfig(TypedDict):
    height: int
    width: int
    words: List[WrittenWord]
    letter_grid: List[List[LetterCell]]


print(str(window.location).split("play.html?game=", 1)[1])
print(decode_data(str(window.location).split("play.html?game=", 1)[1]))
