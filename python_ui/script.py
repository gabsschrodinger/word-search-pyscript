from js import document
from pyodide.ffi.wrappers import add_event_listener
from python_core.tracked_words import written_words, remove_word
from python_core.letter_grid import letter_grid
from python_core.write_words import write_with_retry


def rerender_board():
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

    highlight_words_toggle()


def display_tracked_words() -> None:
    written_words_div = document.querySelector(".written-words")
    written_words_div.replaceChildren()

    for word in written_words:
        new_word = document.createElement("div")
        new_word.setAttribute("class", "written-word")
        new_word_content = document.createTextNode(word["word"])
        new_word.appendChild(new_word_content)

        new_word_remove_btn = document.createElement("div")
        new_word_remove_btn.setAttribute(
            "class", "written-word-remove-btn")
        new_word_remove_btn.id = "remove-" + word["word"]
        remove_word_content = document.createTextNode("X")
        new_word_remove_btn.appendChild(remove_word_content)

        add_event_listener(new_word_remove_btn, "click", lambda e: remove_word(
            e.target.id[7:], display_tracked_words, rerender_board))

        new_word.appendChild(new_word_remove_btn)

        written_words_div.appendChild(new_word)



def submit_word():
    add_word_input = document.querySelector(".add-word-input")
    word_to_add = add_word_input.value

    if word_to_add == None or word_to_add == "":
        return

    write_with_retry(word_to_add.upper(),
                     display_tracked_words, rerender_board)

    add_word_input.value = ""

    rerender_board()


def highlight_words_toggle():
    for letter_row in letter_grid:
        for letter_cell in letter_row:
            class_name = ".coordinate-" + str(letter_cell["coordinate"][0]) + "-" + str(letter_cell["coordinate"][1])
            letter_cell_element = document.querySelector(class_name)

            if document.querySelector(".highlight-input").checked and letter_cell["locked"] > 0:
                letter_cell_element.classList.add("letter-cell-highlighted")
            else:
                letter_cell_element.classList.remove("letter-cell-highlighted")


rerender_board()

add_word_input = document.querySelector(".add-word-input")
add_event_listener(add_word_input, "keydown",
                   lambda e: submit_word() if e.code == "Enter" else None)