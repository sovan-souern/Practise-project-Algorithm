import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to update expression in the entry widget
def update_expression(value):
    entry.insert(tk.END, value)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Setting up the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget for display
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 3),
    ('C', 4, 2), ('=', 5, 0, 4)  # Span "=" button across 4 columns
]

# Creating and placing buttons
for (text, row, col, *cs) in buttons:
    colspan = cs[0] if cs else 1
    if text == '=':
        btn = tk.Button(window, text=text, width=32, height=2, font=("Arial", 18),
                        command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(window, text=text, width=8, height=2, font=("Arial", 18),
                        command=clear_entry)
    else:
        btn = tk.Button(window, text=text, width=8, height=2, font=("Arial", 18),
                        command=lambda val=text: update_expression(val))
    btn.grid(row=row, column=col, columnspan=colspan)

window.mainloop()
