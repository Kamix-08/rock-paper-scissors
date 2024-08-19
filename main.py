from tkinter import *
from PIL import ImageTk, Image
import json

from ai import AI

BG = "#888"

class App:
    def play(self, choice: int):
        prediction = self.ai.predict()

        self.choice.config(text=f"AI chose: {self.names[prediction]}")

        res = self.ai.res(choice, prediction)

        self.games += 1
        self.ai.history.append(choice)

        if res == 0:
            self.result.config(text=f"You won.")
            self.result.config(bg="#00FF00")

            self.loses += 1
        elif res == 1:
            self.result.config(text=f"Draw.")
            self.result.config(bg="#FFFF00")

            self.draws += 1
        else:
            self.result.config(text=f"AI wins.")
            self.result.config(bg="#FF0000")

            self.wins += 1

        self.wins_label.config(text=f"Wins: {self.loses}\n{(100 * self.loses/self.games):.2f}%")
        self.draws_label.config(text=f"Draws: {self.draws}\n{(100 * self.draws/self.games):.2f}%")
        self.loses_label.config(text=f"Loses: {self.wins}\n{(100 * self.wins/self.games):.2f}%")

    def create_ui(self):
        self.title = Label(self.root, text="Choose:", bg=BG, font=("Arial", 25, 'bold'))
        self.title.pack(side=TOP, pady=20)

        self.group = Frame(self.root, bg=BG)
        self.group.pack(expand=True)

        self.images = {} # so that it doesn't get removed by the garbage collector

        self.rock     = self.button(0)
        self.paper    = self.button(1)
        self.scissors = self.button(2)

        self.rock.    grid(row=0, column=0, padx=10)
        self.paper.   grid(row=0, column=1, padx=10)
        self.scissors.grid(row=0, column=2, padx=10)

        self.group.place(relx=.5, rely=.4, anchor='center')

        self.choice = Label(self.root, text="Waiting...", bg=BG, font=("Arial", 15, 'normal'))
        self.choice.place(relx=.5, rely=.6, anchor='center')

        self.stats = Frame(self.root, bg=BG)
        self.stats.pack(fill=X, side=BOTTOM)

        self.wins_label  = Label(self.stats, text= f"Wins: 0\nN/A", bg="#333", fg="#00FF00", font=("Arial", 15, 'normal'))
        self.draws_label = Label(self.stats, text=f"Draws: 0\nN/A", bg="#333", fg="#FFFF00", font=("Arial", 15, 'normal'))
        self.loses_label = Label(self.stats, text=f"Loses: 0\nN/A", bg="#333", fg="#FF0000", font=("Arial", 15, 'normal'))

        self.wins_label. grid(row=0, column=0, sticky='ew', columnspan=1)
        self.draws_label.grid(row=0, column=1, sticky='ew', columnspan=1)
        self.loses_label.grid(row=0, column=2, sticky='ew', columnspan=1)

        for i in range(3):
            self.stats.grid_columnconfigure(i, weight=1)

        self.result = Label(self.root, text="Nothing here yet...", bg=BG, font=("Arial", 15, 'italic'), anchor='center', height=2)
        self.result.pack(fill=X, side=BOTTOM)

    def button(self, id: int) -> Button:
        self.images[id] = ImageTk.PhotoImage(Image.open(f"img/{self.names[id]}.png").resize((100, 100)))

        return Button(self.group, 
                      image=self.images[id], 
                      command=lambda: self.play(choice=id),
                      height=100, width=100)

    def __init__(self):
        self.names = {
            0: "rock",
            1: "paper",
            2: "scissors"
        }

        with open('./data.json', 'r') as file:
            data = json.load(file)

        self.ai = AI(memory=data["memory"], 
                    pattern=data["pattern"], 
                    exponent=data["exponent"])
        
        self.games = 0

        self.wins = 0
        self.draws = 0
        self.loses = 0

        self.root = Tk()
        self.root.title("Rock-Paper-Scissors AI")
        self.root.geometry(f"480x360")
        self.root.config(bg=BG)

        self.root.resizable(False, False)

        self.create_ui()

        self.root.mainloop()

if __name__ == "__main__":
    app = App()