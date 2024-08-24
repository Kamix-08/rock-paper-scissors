from tkinter import *
from PIL import ImageTk, Image
import json

from ai import AI

BG = "#888"

NAMES =  ["rock", "paper", "scissors"]
LABELS = ["Wins", "Draws", "Losses"]
COLORS = [("#00FF00", "#00AA00"), 
          ("#FFFF00", "#AAAA00"), 
          ("#FF0000", "#AA0000")]
TEXTS = ["You won.", "Draw.", "AI won."]

class App:
    def play(self, choice: int):
        self.choice.config(text=f"AI chose: {NAMES[self.prediction]}")

        res = self.ai.res(choice, self.prediction)

        self.games += 1
        self.ai.history.append(choice)

        self.result.config(text=TEXTS[res])
        self.result.config(bg=COLORS[res][1])

        self.values[res] += 1

        for i in range(3):
            self.labels[i].config(text=f"{LABELS[i]}: {self.values[i]}\n{(100 * self.values[i]/self.games):.2f}%")

        self.prediction = self.ai.predict() # predict for the next move in advance

    def create_ui(self):
        self.title = Label(self.root, text="Choose:", bg=BG, font=("Arial", 25, 'bold'))
        self.title.pack(side=TOP, pady=20)

        self.group = Frame(self.root, bg=BG)
        self.group.pack(expand=True)

        self.images = {} # so that it doesn't get removed by the garbage collector

        self.buttons = []
        for i in range(3):
            btn = self.button(i)

            self.buttons.append(btn)
            btn.grid(row=0, column=i, padx=10)

        self.group.place(relx=.5, rely=.4, anchor='center')

        self.choice = Label(self.root, text="Waiting...", bg=BG, font=("Arial", 15, 'normal'))
        self.choice.place(relx=.5, rely=.6, anchor='center')

        self.stats = Frame(self.root, bg=BG)
        self.stats.pack(fill=X, side=BOTTOM)

        self.labels = []
        for i in range(3):
            lab = Label(self.stats, text= f"{LABELS[i]}: 0\nN/A", bg="#333", fg=COLORS[i][0], font=("Arial", 15, 'normal'))

            self.labels.append(lab)
            lab.grid(row=1, column=i, sticky='ew', columnspan=1)

        for i in range(3):
            self.stats.grid_columnconfigure(i, weight=1)

        self.result = Label(self.root, text="Nothing here yet...", bg=BG, font=("Arial", 15, 'italic'), anchor='center', height=2)
        self.result.pack(fill=X, side=BOTTOM)

    def button(self, id: int) -> Button:
        self.images[id] = ImageTk.PhotoImage(Image.open(f"img/{NAMES[id]}.png").resize((100, 100)))

        return Button(self.group, 
                      image=self.images[id], 
                      command=lambda: self.play(choice=id),
                      height=100, width=100)

    def __init__(self):
        with open('./data.json', 'r') as file:
            data = json.load(file)

        self.ai = AI(memory=data["memory"], 
                    pattern=data["pattern"], 
                    exponent=data["exponent"])
        
        self.prediction = self.ai.predict()
        self.games = 0

        self.values = [0, 0, 0]

        self.root = Tk()
        self.root.title("Rock-Paper-Scissors AI")
        self.root.geometry(f"480x360")
        self.root.config(bg=BG)

        self.root.resizable(False, False)

        self.create_ui()

        self.root.mainloop()

if __name__ == "__main__":
    app = App()