from js import document
from write_words import write_word_horizontally, write_word_vertically
from letter_grid import letter_grid
import random
from board import rerender_board


def sidebar_toggle():
    if document.querySelector(".sidebar-inactive") == None:
        document.querySelector(".sidebar").classList.add("sidebar-inactive")
        document.querySelector(".shadow").classList.remove("shadow-on")
        hamburger_container = document.querySelector(
            ".hamburger")
        hamburger_container.classList.remove('hamburger-active')
        hamburger_container.children[0].classList.remove("first-bar")
        hamburger_container.children[1].classList.remove("middle-bar")
        hamburger_container.children[2].classList.remove("last-bar")
    elif document.querySelector(".sidebar-inactive") != None:
        document.querySelector(".sidebar").classList.remove("sidebar-inactive")
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

    random_option = random.randint(1, 2)

    match random_option:
        case 1:
            write_word_horizontally(letter_grid, word_to_add.upper())
        case 2:
            write_word_vertically(letter_grid, word_to_add.upper())

    add_word_input.value = ""

    rerender_board()


rerender_board()
