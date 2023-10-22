import tkinter as tk
from tkinter import messagebox

def calculate():
    num1 = str(entry1.get())
    num2 = str(entry2.get())

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return

    operation = combo.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero!")
            return
        result = num1 / num2
    else:
        messagebox.showerror("Error", "Invalid Operation!")
        return

    result_label.config(text=f"Result: {result}")

app = tk.Tk()
app.title("Simple Calculator")


entry1 = tk.Entry(app)
entry2 = tk.Entry(app)


operations = ["+", "-", "*", "/"]
combo = tk.StringVar(app)
combo.set(operations[0])  # set the default value
operation_dropdown = tk.OptionMenu(app, combo, *operations)


calculate_button = tk.Button(app, text="Calculate", command=calculate)


result_label = tk.Label(app, text="Result: ")


entry1.pack(pady=10)
entry2.pack(pady=10)
operation_dropdown.pack(pady=10)
calculate_button.pack(pady=10)
result_label.pack(pady=20)

app.mainloop()
