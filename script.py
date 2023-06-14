from js import document
import random
import string

board_length = 15
board_height = 15

letter_grid = []

def write_word_horizontally(word: str) -> None:
    random_height = random.randint(0, board_height - 1)
    starting_index = random.randint(0, board_length - 1 - len(word))
    for letter in word:
        letter_grid[random_height][starting_index] = letter
        starting_index += 1

game_board = document.getElementsByClassName("game-board")[0]



for height_index in range(board_height):
    current_row = []
    for length_index in range(board_length):
        current_row.append(random.choice(string.ascii_letters).upper())
    letter_grid.append(current_row)

for i in range(len(letter_grid)):
    current_row = document.createElement("div")
    current_row.setAttribute("class", "letter-grid-row")
    for j in letter_grid[i]:
        letter_div = document.createElement("div")
        letter_div.setAttribute("class", "game-letter-div")
        letter_div_content = document.createTextNode(j)
        letter_div.appendChild(letter_div_content)
        current_row.appendChild(letter_div)
    game_board.appendChild(current_row)


