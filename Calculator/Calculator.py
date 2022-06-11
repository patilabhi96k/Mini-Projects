from tkinter import Tk, Entry, Button, StringVar
import tkinter.font as font

from numpy import size

class Calculator:
    def __init__(self, master):
        # Declaring title for the project
        master.title("Calculator")
        # With the help of geometry function taking number of pixels of screen for project.
        master.geometry('357x420+0+0')
        # Set the backgroung colour for calculator
        master.config(bg='#000')
        # Resizing calculator is not possible.
        master.resizable(False, False)

        self.equation=StringVar()
        self.input_value=''
        Entry(width=20, bg='#fff', font=('Times New Roman Bold', 28), textvariable=self.equation).place(x=0,y=0)

        # myFont = font.Font(family='Tahoma', size=9, weight='bold')

        # Creating buttons for taking input from the user.
        Button(width=11, height=4, text='(', relief='groove', bg='yellow', command=lambda:self.show('(')).place(x=0,y=50)
        Button(width=11, height=4, text=')', relief='groove', bg='yellow', command=lambda:self.show(')')).place(x=90,y=50)
        Button(width=11, height=4, text='%', relief='groove', bg='yellow', command=lambda:self.show('%')).place(x=180,y=50)
        Button(width=11, height=4, text='1', relief='groove', bg='yellow', command=lambda:self.show(1)).place(x=0,y=125)
        Button(width=11, height=4, text='2', relief='groove', bg='yellow', command=lambda:self.show(2)).place(x=90,y=125)
        Button(width=11, height=4, text='3', relief='groove', bg='yellow', command=lambda:self.show(3)).place(x=180,y=125)
        Button(width=11, height=4, text='4', relief='groove', bg='yellow', command=lambda:self.show(4)).place(x=0,y=200)
        Button(width=11, height=4, text='5', relief='groove', bg='yellow', command=lambda:self.show(5)).place(x=90,y=200)
        Button(width=11, height=4, text='6', relief='groove', bg='yellow', command=lambda:self.show(6)).place(x=180,y=200)
        Button(width=11, height=4, text='7', relief='groove', bg='yellow', command=lambda:self.show(7)).place(x=0,y=275)
        Button(width=11, height=4, text='8', relief='groove', bg='yellow', command=lambda:self.show(8)).place(x=180,y=275)
        Button(width=11, height=4, text='9', relief='groove', bg='yellow', command=lambda:self.show(9)).place(x=90,y=275)
        Button(width=11, height=4, text='0', relief='groove', bg='yellow', command=lambda:self.show(0)).place(x=90,y=350)
        Button(width=11, height=4, text='.', relief='groove', bg='yellow', command=lambda:self.show('.')).place(x=180,y=350)
        Button(width=11, height=4, text='+', relief='groove', bg='yellow', command=lambda:self.show('+')).place(x=270,y=275)
        Button(width=11, height=4, text='-', relief='groove', bg='yellow', command=lambda:self.show('-')).place(x=270,y=200)
        Button(width=11, height=4, text='/', relief='groove', bg='yellow', command=lambda:self.show('/')).place(x=270,y=50)
        Button(width=11, height=4, text='*', relief='groove', bg='yellow', command=lambda:self.show('*')).place(x=270,y=125)
        Button(width=11, height=4, text='=', relief='groove', bg='yellow', command=self.solve).place(x=270,y=350)
        Button(width=11, height=4, text='C', relief='groove', bg='red', command=self.clear).place(x=0,y=350)

    # Function for input window
    def show(self, value):
        self.input_value+=str(value)
        self.equation.set(self.input_value)

    # Declaring screen clear function
    def clear(self):
        self.input_value=''
        self.equation.set(self.input_value)

    # Declaring the result of arithmetic calculations.
    def solve(self):
        result=eval(self.input_value)
        self.equation.set(result)

# Main function
base = Tk()
Calculator=Calculator(base)
base.mainloop()
