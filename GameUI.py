from matplotlib.style.core import available

from Game import Game
import tkinter as tk
from tkinter import ttk
class GameUI:
    def __init__(self,root):
        self.game = Game()
        self.text = ttk.Label(root,text="",wraplength=300)
        self.text.pack(pady=10)

        self.buttons ={}
        button_frame = ttk.Frame(root)
        button_frame.pack()
        for d in ['north','south','east','west']:
            btn = ttk.Button(root, text=d.capitalize(),
                             command=lambda dir=d: self.move(dir))
            btn.pack(side='left',padx=5)
            self.buttons[d] = btn
        self.update_ui()
    def move(self,direction):
        self.game.move(direction)
        self.update_ui()

    def update_ui(self):
        # Update room description
        self.text.config(text=self.game.get_description())
        # Get valid directions
        available = self.game.get_available_directions()

        # Enable/Disable buttons
        for direction, button in self.buttons.items():
            if direction in available:
                button.state(["!disabled"])
            else:
                button.state(["disabled"])