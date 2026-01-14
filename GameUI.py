
from Game import Game
import tkinter as tk
from tkinter import ttk
class GameUI:
    def __init__(self,root):
        self.game = Game()
        # This text is for creating space it's a placebo effect on logic code
        self.text = ttk.Label(root,text="",wraplength=300)
        self.text.pack(pady=10)
        # Main frame that get the whole window
        main_frame = ttk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        # LEFT SIDE (game)
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True)

        self.text = ttk.Label(left_frame, text="", wraplength=300)
        self.text.pack(pady=20)

        button_frame = ttk.Frame(left_frame)
        button_frame.pack(pady=10)

        self.buttons ={}
        for d in ['north','south','east','west']:
            btn = ttk.Button(button_frame, text=d.capitalize(),
                             command=lambda dir=d: self.move(dir))
            btn.pack(side='left',padx=15,pady=20)
            self.buttons[d] = btn

        # RIGHT SIDE (inventory)
        self.inventory_frame = ttk.Frame(main_frame, relief="sunken", padding=10)

        self.inventory_frame.pack(side="right", fill="y",padx=20,pady=20)

        self.inventory_title_frame = ttk.Frame(self.inventory_frame, relief="sunken", padding=10)
        self.inventory_title_frame.pack()
        ttk.Label(self.inventory_title_frame, text="Inventory").pack(side="top")

        self.inventory_items_frame = ttk.Frame(self.inventory_frame)
        self.inventory_items_frame.pack(anchor="nw")
        self.update_ui()
    def move(self,direction):
        self.game.move(direction)
        self.update_ui()

    def update_inventory_ui(self):
        # Clear  old items
        for widget in self.inventory_items_frame.winfo_children():
            widget.destroy()
        # Add current items
        for item_name in self.game.inventory:
            ttk.Label(self.inventory_items_frame,text=f"-{item_name}").pack(anchor="w")


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
        self.update_inventory_ui()