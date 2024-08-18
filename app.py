from tkinter import *

TITLE = "Rock-Paper-Scissors AI"
GEOMETRY = (800, 600)
RESIZABLE = (False, False)
BG = "#888"

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title(TITLE)
        self.root.geometry(f"{GEOMETRY[0]}x{GEOMETRY[1]}")
        self.root.config(bg=BG)

        self.root.resizable(RESIZABLE[0], RESIZABLE[1])

        self.root.mainloop()