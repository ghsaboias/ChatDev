'''
This is the main file of the minesweeper game. It handles the game flow and user interactions.
'''
import tkinter as tk
from game import Game
class MinesweeperApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Minesweeper")
        self.master.resizable(False, False)
        self.start_screen()
    def start_screen(self):
        logo_label = tk.Label(self.master, text="Minesweeper", font=("Arial", 24))
        logo_label.pack()
        start_button = tk.Button(self.master, text="Start", font=("Arial", 16), command=self.game_screen)
        start_button.pack()
    def game_screen(self):
        self.game = Game(self.master)
        self.game.pack()
    def game_over_screen(self):
        self.game.game_over()
    def try_again(self):
        self.master.destroy()
        root = tk.Tk()
        app = MinesweeperApp(root)
        root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = MinesweeperApp(root)
    root.mainloop()