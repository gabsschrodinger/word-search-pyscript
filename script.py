from js import document
from write_words import write_word_horizontally, write_word_vertically
from letter_grid import generate_random_letter_grid
import random

board_length = 15
board_height = 15

letter_grid = generate_random_letter_grid(board_length, board_height)


def sidebar_toggle():
    if document.querySelector(".sidebar-inactive") == None:
        document.querySelector(".sidebar").classList.add("sidebar-inactive")
        document.querySelector(
            ".hamburger").classList.remove('hamburger-active')
        document.querySelector(".shadow").classList.remove("shadow-on")
    elif document.querySelector(".sidebar-inactive") != None:
        document.querySelector(".sidebar").classList.remove("sidebar-inactive")
        document.querySelector(".hamburger").classList.add("hamburger-active")
        document.querySelector(".shadow").classList.add("shadow-on")


def rerender_board():
    game_board = document.querySelector(".game-board")
    game_board.replaceChildren()

    for i in range(len(letter_grid)):
        current_row = document.createElement("div")
        current_row.setAttribute("class", "letter-grid-row")
        for j in letter_grid[i]:
            letter_div = document.createElement("div")
            letter_div.setAttribute("class", "game-letter-div")
            letter_div_content = document.createTextNode(j["value"])
            letter_div.appendChild(letter_div_content)
            current_row.appendChild(letter_div)
        game_board.appendChild(current_row)


def submit_word():
    add_word_input = document.querySelector(".add-word-input")
    word_to_add = add_word_input.value

    if word_to_add == None or word_to_add == "":
        return

    random_option = random.randint(1, 2)

    match random_option:
        case 1:
            write_word_horizontally(letter_grid, word_to_add)
        case 2:
            write_word_vertically(letter_grid, word_to_add)

    add_word_input.value = ""

    rerender_board()


rerender_board()
