from js import document
from pyodide.ffi.wrappers import add_event_listener
from tracked_words import written_words, remove_word
from letter_grid import letter_grid
from write_words import write_with_retry


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
        remove_word_content = document.createTextNode("X")
        new_word_remove_btn.appendChild(remove_word_content)

        add_event_listener(new_word_remove_btn, "click",
                           lambda _: remove_word(word["word"], display_tracked_words, rerender_board))

        new_word.appendChild(new_word_remove_btn)

        written_words_div.appendChild(new_word)


def sidebar_toggle():
    if document.querySelector(".sidebar-inactive") == None:
        document.querySelector(
            ".sidebar").classList.add("sidebar-inactive")
        document.querySelector(".shadow").classList.remove("shadow-on")
        hamburger_container = document.querySelector(
            ".hamburger")
        hamburger_container.classList.remove('hamburger-active')
        hamburger_container.children[0].classList.remove("first-bar")
        hamburger_container.children[1].classList.remove("middle-bar")
        hamburger_container.children[2].classList.remove("last-bar")
    elif document.querySelector(".sidebar-inactive") != None:
        document.querySelector(
            ".sidebar").classList.remove("sidebar-inactive")
        document.querySelector(".shadow").classList.add("shadow-on")
        hamburger_container = document.querySelector(
            ".hamburger")
        hamburger_container.classList.add("hamburger-active")
        hamburger_container.children[0].classList.add("first-bar")
        hamburger_container.children[1].classList.add("middle-bar")
        hamburger_container.children[2].classList.add("last-bar")


def shadow_sidebar_toggle():
    if document.querySelector(".shadow-on") != None:
        sidebar_toggle()


def submit_word():
    add_word_input = document.querySelector(".add-word-input")
    word_to_add = add_word_input.value

    if word_to_add == None or word_to_add == "":
        return

    write_with_retry(word_to_add.upper(),
                     display_tracked_words, rerender_board)

    add_word_input.value = ""

    rerender_board()


rerender_board()
