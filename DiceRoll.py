import tkinter as tk
import random

class DiceRollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll Simulator")
        
        #Labels to display dice values
        self.dice1_label = tk.Label(self.root, text="Dice 1: ", font=("Arial", 20))
        self.dice1_label.pack(pady=10)
        
        self.dice2_label = tk.Label(self.root, text="Dice 2: ", font=("Arial", 20))
        self.dice2_label.pack(pady=10)
        
        #Roll Dice button
        self.roll_button = tk.Button(self.root, text="Roll the Dice", command=self.roll_dice, font=("Arial", 16))
        self.roll_button.pack(pady=20)
        
        #Quit button
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, font=("Arial", 16))
        self.quit_button.pack(pady=10)
    
    def roll_dice(self):
        #Generate random values for the two dice
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        #Update the dice labels
        self.dice1_label.config(text=f"Dice 1: {dice1}")
        self.dice2_label.config(text=f"Dice 2: {dice2}")

#Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollApp(root)
    root.mainloop()
