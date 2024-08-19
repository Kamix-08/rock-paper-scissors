from tkinter import *
from PIL import ImageTk, Image

BG = "#888"

class App:
    def create_ui(self):
        self.title = Label(self.root, text="Choose:", bg=BG, font=("Arial", 25, 'bold'))
        self.title.pack(side=TOP, pady=20)

        self.group = Frame(self.root, bg=BG)
        self.group.pack(expand=True)

        self.images = {}

        self.rock = self.button("rock")
        self.paper = self.button("paper")
        self.scissors = self.button("scissors")

        self.rock.grid(row=0, column=0, padx=10)
        self.paper.grid(row=0, column=1, padx=10)
        self.scissors.grid(row=0, column=2, padx=10)

        self.group.place(relx=.5, rely=.5, anchor='center')

        self.result = Label(self.root, text="", bg=BG, font=("Arial", 20, 'italic'), anchor='center', height=2)
        self.result.pack(side=BOTTOM, fill=X)

    def button(self, name):
        self.images[name] = ImageTk.PhotoImage(Image.open(f"img/{name}.png").resize((100, 100)))

        return Button(self.group, 
                      image=self.images[name], 
                      height=100, width=100)

    def __init__(self):
        self.root = Tk()
        self.root.title("Rock-Paper-Scissors AI")
        self.root.geometry(f"480x360")
        self.root.config(bg=BG)

        self.root.resizable(False, False)

        self.create_ui()

        self.root.mainloop()