import tkinter as tk
from tkinter import ttk
from cli_calculator import safe_eval

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")
        self.expression = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = ttk.Entry(self, textvariable=self.expression, font=("Arial", 20), justify="right")
        entry.pack(fill="x", padx=10, pady=10, ipady=10)

        frame = ttk.Frame(self)
        frame.pack(padx=10, pady=10)

        buttons = [
            ("7","8","9","/"),
            ("4","5","6","*"),
            ("1","2","3","-"),
            ("0",".","=","+"),
        ]

        for r,row in enumerate(buttons):
            for c,char in enumerate(row):
                btn = ttk.Button(frame, text=char, command=lambda ch=char: self.on_button(ch))
                btn.grid(row=r, column=c, padx=5, pady=5, ipadx=10, ipady=10)

        clear_btn = ttk.Button(self, text="Clear", command=self.clear)
        clear_btn.pack(fill="x", padx=10, pady=10)

    def on_button(self, char):
        if char == "=":
            self.calculate()
        else:
            self.expression.set(self.expression.get() + char)

    def clear(self):
        self.expression.set("")

    def calculate(self):
        try:
            result = safe_eval(self.expression.get())
            self.expression.set(str(result))
        except:
            self.expression.set("Error")

if __name__ == "__main__":
    Calculator().mainloop()
