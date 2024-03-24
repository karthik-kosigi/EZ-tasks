import tkinter as tk

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("")

        # Entry to display the result
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 20), justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('⌫', 5, 1)  # Clear and Backspace buttons
        ]

        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, width=5, height=2,
                               font=('Arial', 14, 'bold'), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")

        self.root.mainloop()

    def on_button_click(self, text):
        if text == '=':
            self.calculate()
        elif text == 'C':
            self.clear()
        elif text == '⌫':
            self.backspace()
        else:
            self.expression += text
            self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.result_var.set(result)
        except ZeroDivisionError:
            self.result_var.set("Cannot divide by zero!")
        except Exception as e:
            self.result_var.set("Error")
        finally:
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.result_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def update_display(self):
        self.result_var.set(self.expression)


def main():
    root = tk.Tk()
    app = CalculatorGUI(root)

if __name__ == "__main__":
    main()
