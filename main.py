import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        # Create the input field
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        input_field.grid(row=0, column=0)

        # Create buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, column) in buttons:
            self.create_button(button_frame, text, row, column)

    def create_button(self, frame, text, row, column):
        button = tk.Button(frame, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char)
        
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
