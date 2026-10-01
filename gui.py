import tkinter as tk
from tkinter import ttk
from lexer import Lexer
from parser import Parser


def calculate(expression):
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    result = parser.parse_expression()
    return result


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("350x450")
        self.root.resizable(False, False)

        self.expression = ""

        # Поле ввода
        self.entry = ttk.Entry(root, font=('Consolas', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=5, sticky='nsew', padx=5, pady=5)
        self.entry.focus()

        # Результат
        self.result_label = ttk.Label(root, text="Результат: ", font=('Arial', 12))
        self.result_label.grid(row=1, column=0, columnspan=5, sticky='w', padx=5, pady=5)

        # Кнопки
        buttons = [
            ['C', '←', '(', ')', '/'],
            ['7', '8', '9', ',', '*'],
            ['4', '5', '6', '|', '-'],
            ['1', '2', '3', 'min', '+'],
            ['', '0', '.', '=', ''],
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                if not text:
                    continue

                btn = ttk.Button(
                    root, text=text,
                    command=lambda t=text: self.on_click(t)
                )
                btn.grid(row=r + 2, column=c, sticky='nsew', padx=2, pady=2)

        # Сетка
        for i in range(5):
            self.root.columnconfigure(i, weight=1)
        for i in range(7):
            self.root.rowconfigure(i, weight=1)

        # Бинды клавиатуры
        self.root.bind('<Key>', self.on_key)
        self.root.bind('<Return>', lambda e: self.on_click('='))
        self.root.bind('<BackSpace>', lambda e: self.on_click('←'))
        self.root.bind('<Escape>', lambda e: self.on_click('C'))

    def on_click(self, char):
        """нажатия на кнопки приложения"""
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
            self.result_label.config(text="Результат: ", foreground='black')
        elif char == '←':
            self.expression = self.expression[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
        elif char == '=':
            self.calc()
        else:
            self.expression += char
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)

        self.entry.focus()

    def on_key(self, event):
        """Ввод символов с клавиатуры"""
        char = event.char
        if char in '0123456789+-*/|(),.min':
            self.on_click(char)

    def calc(self):
        """Запуск вычисления выражения"""
        try:
            if not self.expression.strip():
                self.result_label.config(text=f"Результат: 0", foreground='black')
                return
            result = calculate(self.expression)
            if isinstance(result, float) and result == int(result):
                result = int(result)
            self.result_label.config(text=f"Результат: {result}", foreground='black')
        except Exception as e:
            self.result_label.config(text=f"Ошибка: {e}", foreground='red')


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()