# ui.py
import tkinter as tk
from calculator import add, subtract, multiply, divide

class CalculatorUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.configure(bg="black")

        # Entry display
        self.entry = tk.Entry(
            self.root, width=20, font=("Arial", 18),
            bg="black", fg="white", justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons (numbers black/white, operators white/black)
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)  # Clear button
        ]

        for (text, row, col) in buttons:
            if text.isdigit() or text == ".":  # Numbers and decimal
                bg_color, fg_color = "black", "white"
            else:  # Operators (+ - × ÷ = C)
                bg_color, fg_color = "white", "black"

            tk.Button(
                self.root,
                text=text,
                width=5,
                height=2,
                font=("Arial", 16, "bold"),
                bg=bg_color,
                fg=fg_color,
                command=lambda val=text: self.on_button_click(val)
            ).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == "=":
            try:
                expression = self.entry.get()
                # Replace symbols with Python equivalents
                expression = expression.replace("×", "*").replace("÷", "/")
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "C":  # Clear button
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)

    def run(self):
        self.root.mainloop()
