import tkinter as tk

CALC_BG = "#a2bbcf"
CALC_FG = "#1d3849"

WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"

SMALL_FONT = ("Technology", 16)
LARGE_FONT = ("Technology", 40, "bold")
DIGIT_FONT = ("Technology", 24, "bold")
DEFAULT_FONT = ("Technology", 20)

digits = {
    7: (1, 1),
    8: (1, 2),
    9: (1, 3),
    4: (2, 1),
    5: (2, 2),
    6: (2, 3),
    1: (3, 1),
    2: (3, 2),
    3: (3, 3),
    0: (4, 2),
    '.': (4, 1)
}


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total = ""
        self.current = ""

        self.display = self.create_display()
        self.buttons = self.create_buttons()

        self.total_label, self.label = self.create_display_labels()

        self.digits = digits
        self.operations = { "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons.rowconfigure(x, weight=1)
            self.buttons.columnconfigure(x, weight=1)
        
        self.create_digit_buttons()


        self.create_op_buttons()

        self.create_clear_button()
        self.create_eq_button()
        self.create_back_button()
        self.create_sqrt_button()
        self.create_square_button()

        self.bind_keys()
    
    def create_display(self):
        frame = tk.Frame(self.window, height=200, bg=CALC_BG)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_buttons(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_display_labels(self):
        total_label = tk.Label(self.display, text=self.total, anchor=tk.E, bg=CALC_BG, fg=CALC_FG, padx=24, font=SMALL_FONT)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display, text=self.current, anchor=tk.E, bg=CALC_BG, fg=CALC_FG, padx=24, font=LARGE_FONT)
        label.pack(expand=True, fill="both")

        return total_label, label

    def add_to_expression(self, value):
        self.current += str(value)
        self.update_current()
    
    def add_op(self, op):
        self.current += op
        self.total += self.current
        self.current = ""
        self.update_current()
        self.update_total()
    
    def remove_last(self):
        self.current = self.current[:-1]
        self.total = self.total[:-1]
        self.update_current()
        self.update_total()
    
    def clear(self):
        self.current = ""
        self.total = ""
        self.update_current()
        self.update_total()
    
    def evaluate(self):
        self.total += self.current
        self.update_total()

        try:
            self.current = str(eval(self.total))
            self.total = ""
        except Exception as e:
            self.current = "Error"
        finally:
            self.update_current()
    
    def square(self):
        self.current = str(eval(f"{self.current}**2"))
        self.update_current()
    
    def sqrt(self):
        self.current = str(eval(f"{self.current}**0.5"))
        self.update_current()

    def create_digit_buttons(self):
        for digit, idx in self.digits.items():
            button = tk.Button(self.buttons, text=str(digit), bg=WHITE, fg=CALC_FG, font=DIGIT_FONT, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=idx[0], column=idx[1], sticky=tk.NSEW)
    
    def create_op_buttons(self):
        i = 0
        for arithmetic, op in self.operations.items():
            button = tk.Button(self.buttons, text=op, bg=OFF_WHITE, fg=CALC_FG, font=DEFAULT_FONT, borderwidth=0, command=lambda x=arithmetic: self.add_op(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
    
    def create_clear_button(self):
        button = tk.Button(self.buttons, text="C", bg=OFF_WHITE, fg=CALC_FG, font=DEFAULT_FONT, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
    
    def create_square_button(self):
        button = tk.Button(self.buttons, text="x\u00b2", bg=OFF_WHITE, fg=CALC_FG, font=DEFAULT_FONT, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
    
    def create_sqrt_button(self):
        button = tk.Button(self.buttons, text="\u221a", bg=OFF_WHITE, fg=CALC_FG, font=DEFAULT_FONT, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)
    
    def create_back_button(self):
        button = tk.Button(self.buttons, text="⌫", bg=OFF_WHITE, fg=CALC_FG, font=DEFAULT_FONT, borderwidth=0, command=self.remove_last)
        button.grid(row=4, column=3, sticky=tk.NSEW)
    
    def create_eq_button(self):
        button = tk.Button(self.buttons, text="=", bg="#CDDEFF", fg=CALC_FG, font=DEFAULT_FONT, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=4, sticky=tk.NSEW)
    
    def update_total(self):
        expression = self.total
        for op, symbol in self.operations.items():
            expression = expression.replace(op, f' {symbol} ')

        self.total_label.config(text=expression)

    def update_current(self):
        self.label.config(text=self.current[:11])
    
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())

        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(str(key), lambda event, op=key: self.add_op(op))
    
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()