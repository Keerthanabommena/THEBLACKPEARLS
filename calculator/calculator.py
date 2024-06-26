from tkinter import *
import math

# Global variables for memory function
memory = 0
expression = ""

# Function to update the input field when a button is pressed
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except ZeroDivisionError:
        equation.set("Cannot divide by zero")
        expression = ""
    except Exception:
        equation.set("Invalid input")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to calculate square root
def sqrt():
    global expression
    try:
        total = str(math.sqrt(float(expression)))
        equation.set(total)
        expression = total
    except ValueError:
        equation.set("Invalid input")
        expression = ""

# Function to add to memory
def mem_add():
    global memory, expression
    try:
        memory += float(equation.get())
        expression = ""
        equation.set("")
    except ValueError:
        equation.set("Invalid input")
        expression = ""

# Function to recall memory
def mem_recall():
    global memory
    equation.set(memory)
    expression = str(memory)

# Function to clear memory
def mem_clear():
    global memory
    memory = 0
    equation.set("")

# Creating the main window
gui = Tk()
gui.title("Calculator")
gui.configure(bg="#2e2e2e")
gui.resizable(False, False)

equation = StringVar()

# Create the output field with enhanced look
output_frame = Frame(gui, bg="#2e2e2e")
output_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

input_field = Entry(output_frame, textvariable=equation, font=('Arial', 20), bd=0, insertwidth=2, width=14, borderwidth=0, bg="#4e4e4e", fg="#ffffff", justify='right')
input_field.grid(row=0, column=0)

# Define button styles
button_font = ('Arial', 18)
button_bg = "#00a2e8"
button_fg = "#ffffff"
button_active_bg = "#007acc"
button_active_fg = "#ffffff"
special_button_bg = "#ff4081"

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('√', 5, 0), ('^', 5, 1), ('.', 5, 2), ('M+', 5, 3),
    ('MR', 6, 0), ('MC', 6, 1)
]

# Function to handle button clicks
def on_click(value):
    if value == '=':
        equalpress()
    elif value == 'C':
        clear()
    elif value == '√':
        sqrt()
    elif value == '^':
        press('**')
    elif value == 'M+':
        mem_add()
    elif value == 'MR':
        mem_recall()
    elif value == 'MC':
        mem_clear()
    else:
        press(value)

# Create buttons
for (text, row, col) in buttons:
    bg_color = button_bg if text not in ['C', '=', '√', 'M+', 'MR', 'MC'] else special_button_bg
    Button(gui, text=text, font=button_font, bg=bg_color, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda text=text: on_click(text), height=2, width=6).grid(row=row, column=col, padx=5, pady=5)

# Start the GUI
gui.mainloop()
