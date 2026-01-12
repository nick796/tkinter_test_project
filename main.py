import tkinter as tk
from tkinter import ttk
from Game import Game
from tkinter_test_project.GameUI import GameUI

game = Game()
print(game.get_description())
print(game.get_available_directions())

root = tk.Tk()
root.title("Text Adventure")

GameUI(root)
root.mainloop()