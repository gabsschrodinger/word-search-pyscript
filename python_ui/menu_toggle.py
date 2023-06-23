from js import document
from pyodide.ffi.wrappers import add_event_listener


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


def shadow_toggle():
    if document.querySelector(".shadow-on") != None:
        sidebar_toggle()


add_event_listener(document.querySelector("body"), "keydown", lambda e: sidebar_toggle(
) if e.code == "Escape" and document.querySelector(".shadow-on") != None else None)
