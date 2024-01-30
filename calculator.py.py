# This line imports all the classes and functions from the tkinter module, allowing us to use them in our code.
from tkinter import *

# This variable expression will store the mathematical expression that the user enters.
expression = ''

# This function is called when a button representing a digit or an operator is clicked.
# It updates the expression variable by appending the clicked value, converts it to a string, 
# and sets the value of the equation variable, which is used to update the display field.
def press(userinput):
    global expression
    expression = expression + str(userinput)
    equation.set(expression)

# This function is called when the equal button (=) is clicked. It evaluates the expression using the eval() function, 
# which interprets the expression as a Python code and returns the result. If the expression is valid,
#  it sets the result as the value of the equation variable and updates the expression variable.
#  If there is an error (e.g., dividing by zero), it sets the equation variable to "error".
def equalPress():
    try:
        global expression
        result = eval(expression)
        equation.set(result)
        expression = str(result)
    except:
        equation.set("error")

# This function is called when the clear button (c) is clicked. It clears the expression variable and 
# sets the equation variable to an empty string, effectively clearing the display.
def clear():
    global expression
    expression = ""
    equation.set(expression)

# These lines create the main window of the calculator application using the Tk() class from the tkinter module. 
# It sets the window title to "simple calculator" and the window size to 280x250 pixels.
gui = Tk()
gui.title("simple calculator")
gui.geometry("280x250")

# These lines create a label widget to display the title of the calculator. 
# It sets the text to "Simple calculator", the foreground color to blue, and the font to "century 18 bold". 
# The grid() method is used to specify the layout of the widget within the grid system of the window.
titleLabel = Label(gui, text="Simple calculator", fg="blue", font="century 18 bold")
titleLabel.grid(columnspan=4, pady=20)

# These lines create an entry widget, which is used as the display field for the calculator. 
# The StringVar() class is used to create a special variable (equation) that will be linked to the entry widget. 
# The grid() method is used to specify the layout of the widget within the grid system of the window.
equation = StringVar()
expressionField = Entry(gui, textvariable=equation)
expressionField.grid(columnspan=4, padx=5, pady=10, ipadx=70)

# These lines create the buttons for digits (0-9), operators (+, -, *, /), decimal point (.), equal 😊), and clear (c). 
# The Button() class is used to create each button, and the command parameter specifies the function to be called when the button is clicked. 
# The grid() method is used to specify the layout of the buttons within the grid system of the window.
btn1 = Button(gui, text=' 1 ', command=lambda: press(1), height=1, width=7)
btn1.grid(row=2, column=0)

btn2 = Button(gui, text=' 2 ', command=lambda: press(2), height=1, width=7)
btn2.grid(row=2, column=1)

btn3 = Button(gui, text=' 3 ', command=lambda: press(3), height=1, width=7)
btn3.grid(row=2, column=2)

btn4 = Button(gui, text=' 4 ', command=lambda: press(4), height=1, width=7)
btn4.grid(row=3, column=0)

btn5 = Button(gui, text=' 5 ', command=lambda: press(5), height=1, width=7)
btn5.grid(row=3, column=1)

btn6 = Button(gui, text=' 6 ', command=lambda: press(6), height=1, width=7)
btn6.grid(row=3, column=2)

btn7 = Button(gui, text=' 7 ', command=lambda: press(7), height=1, width=7)
btn7.grid(row=4, column=0)

btn8 = Button(gui, text=' 8 ', command=lambda: press(8), height=1, width=8)
btn8.grid(row=4, column=1)

btn9 = Button(gui, text=' 9 ', command=lambda: press(9), height=1, width=8)
btn9.grid(row=4, column=2)

btn0 = Button(gui, text=' 0 ', command=lambda: press(0), height=1, width=8)
btn0.grid(row=5, column=0)

dotBtn = Button(gui, text=' . ', command=lambda: press('.'), height=1, width=8)
dotBtn.grid(row=5, column=1)

equalBtn = Button(gui, text=' = ', command=lambda: equalPress(), height=1, width=8, bg="blue", fg="white")
equalBtn.grid(row=5, column=2)

PlusBtn = Button(gui, text=' +', command=lambda: press('+'), height=1, width=8)
PlusBtn.grid(row=2, column=3)

minusBtn = Button(gui, text=' - ', command=lambda: press('-'), height=1, width=8)
minusBtn.grid(row=3, column=3)

multiplyBtn = Button(gui, text=' * ', command=lambda: press('*'), height=1, width=8)
multiplyBtn.grid(row=4, column=3)

dividBtn = Button(gui, text='  / ', command=lambda: press('/'), height=1, width=8)
dividBtn.grid(row=5, column=3)

clearBtn = Button(gui, text='  c ', command=lambda: clear(), height=1, width=8)
clearBtn.grid(row=6, column=0)

# This line starts the main event loop of the GUI, which listens for user interactions and updates the display accordingly. 
# It keeps the window open and responsive until it is closed by the use
gui.mainloop()
