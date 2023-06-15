from js import document
from write_words import write_word_horizontally, write_word_vertically
from letter_grid import generate_random_letter_grid

board_length = 15
board_height = 15

letter_grid = generate_random_letter_grid(board_length, board_height)
letter_grid = write_word_horizontally(letter_grid, "OOOOOOOO")
letter_grid = write_word_vertically(letter_grid, "OOOOOOOO")

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

rerender_board()