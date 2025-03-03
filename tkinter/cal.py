from tkinter import *

# Function to update the expression on the display
def btn_click(char):
    global expression
    expression += str(char)
    input_field.set(expression)

# Function to clear the display
def btn_clear():
    global expression
    expression = ""
    input_field.set("")

# Function to evaluate the expression
def btn_equal():
    try:
        global expression
        result = str(eval(expression))
        input_field.set(result)
        expression = result
    except:
        input_field.set("Error")

# Main
expression = ""
root = Tk()
root.title("CALCULATOR")  # Set the window title here

# Input field
input_field = StringVar()
input_entry = Entry(root, textvariable=input_field)
input_entry.grid(columnspan=4, ipadx=70)

# Buttons (rest of the code remains the same)

# Buttons
button_7 = Button(root, text="7", command=lambda: btn_click(7))
button_7.grid(row=1, column=0)
button_8 = Button(root, text="8", command=lambda: btn_click(8))
button_8.grid(row=1, column=1)
button_9 = Button(root, text="9", command=lambda: btn_click(9))
button_9.grid(row=1, column=2)
button_div = Button(root, text="/", command=lambda: btn_click("/"))
button_div.grid(row=1, column=3)

button_4 = Button(root, text="4", command=lambda: btn_click(4))
button_4.grid(row=2, column=0)
button_5 = Button(root, text="5", command=lambda: btn_click(5))
button_5.grid(row=2, column=1)
button_6 = Button(root, text="6", command=lambda: btn_click(6))
button_6.grid(row=2, column=2)
button_mul = Button(root, text="*", command=lambda: btn_click("*"))
button_mul.grid(row=2, column=3)

button_1 = Button(root, text="1", command=lambda: btn_click(1))
button_1.grid(row=3, column=0)
button_2 = Button(root, text="2", command=lambda: btn_click(2))
button_2.grid(row=3, column=1)
button_3 = Button(root, text="3", command=lambda: btn_click(3))
button_3.grid(row=3, column=2)
button_sub = Button(root, text="-", command=lambda: btn_click("-"))
button_sub.grid(row=3, column=3)

button_0 = Button(root, text="0", command=lambda: btn_click(0))
button_0.grid(row=4, column=0)
button_dot = Button(root, text=".", command=lambda: btn_click("."))
button_dot.grid(row=4, column=1)
button_clear = Button(root, text="C", command=btn_clear)
button_clear.grid(row=4, column=2)
button_add = Button(root, text="+", command=lambda: btn_click("+"))
button_add.grid(row=4, column=3)

button_equal = Button(root, text="=", command=btn_equal)
button_equal.grid(columnspan=4)

root.mainloop()
