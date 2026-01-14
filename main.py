import tkinter as tk
from tkinter import ttk
from Game import Game
from tkinter_test_project.GameUI import GameUI

root = tk.Tk()
root.geometry('700x300')
root.title("Text Adventure")

GameUI(root)
root.mainloop()