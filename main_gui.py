from Backend.parser import Parser
from Backend.lexer import Lexer
from Frontend.gui import CalculatorGUI
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()