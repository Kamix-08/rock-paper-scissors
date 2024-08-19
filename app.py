from tkinter import *
from PIL import ImageTk, Image

from ai import AI

BG = "#888"

class App:
    def play(self, choice: int):
        res = self.ai.res(choice, self.ai.predict())

        self.games += 1
        self.ai.history.append(choice)

        if res == 0:
            self.result.config(text=f"AI loses. ({self.games} : {(100 * self.wins/self.games):.2f}%)")
            self.result.config(bg="#FF0000")
        elif res == 1:
            self.result.config(text=f"AI draws. ({self.games} : {(100 * self.wins/self.games):.2f}%)")
            self.result.config(bg="#FFFF00")
        else:
            self.wins += 1

            self.result.config(text=f"AI wins. ({self.games} : {(100 * self.wins/self.games):.2f}%)")
            self.result.config(bg="#00FF00")

    def create_ui(self):
        self.title = Label(self.root, text="Choose:", bg=BG, font=("Arial", 25, 'bold'))
        self.title.pack(side=TOP, pady=20)

        self.group = Frame(self.root, bg=BG)
        self.group.pack(expand=True)

        self.images = {} # so that it doesn't get removed by the garbage collector

        self.rock     = self.button("rock",     0)
        self.paper    = self.button("paper",    1)
        self.scissors = self.button("scissors", 2)

        self.rock.grid(row=0, column=0, padx=10)
        self.paper.grid(row=0, column=1, padx=10)
        self.scissors.grid(row=0, column=2, padx=10)

        self.group.place(relx=.5, rely=.5, anchor='center')

        self.result = Label(self.root, text="Nothing here yet...", bg="#999", font=("Arial", 15, 'italic'), anchor='center', height=2)
        self.result.pack(side=BOTTOM, fill=X)

    def button(self, name: str, id: int) -> Button:
        self.images[name] = ImageTk.PhotoImage(Image.open(f"img/{name}.png").resize((100, 100)))

        return Button(self.group, 
                      image=self.images[name], 
                      command=lambda: self.play(choice=id),
                      height=100, width=100)

    def __init__(self):
        self.ai = AI(memory=250, 
                     pattern=50, 
                     exponent=2)
        
        self.games = 0
        self.wins = 0

        self.root = Tk()
        self.root.title("Rock-Paper-Scissors AI")
        self.root.geometry(f"480x360")
        self.root.config(bg=BG)

        self.root.resizable(False, False)

        self.create_ui()

        self.root.mainloop()