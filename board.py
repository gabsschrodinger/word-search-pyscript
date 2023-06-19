from js import document
from letter_grid import letter_grid

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