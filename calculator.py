import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result = "Error: Divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Select operation"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

# GUI window
window = tk.Tk()
window.title("Simple GUI Calculator")
window.geometry("300x250")

# Entry for number 1
entry1 = tk.Entry(window, width=15)
entry1.pack(pady=5)

# Entry for number 2
entry2 = tk.Entry(window, width=15)
entry2.pack(pady=5)

# Operation dropdown
operation_var = tk.StringVar()
operation_var.set("Add")  # default
operation_menu = tk.OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.pack(pady=5)

# Calculate button
calc_button = tk.Button(window, text="Calculate", command=calculate)
calc_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)

# Run the app
window.mainloop()
