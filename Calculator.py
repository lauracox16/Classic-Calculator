from tkinter import *
import tkinter as tk


popUp = Tk()                       # Creating pop up window
popUp.geometry("312x400")
popUp.title("Calculator")
popUp.resizable(0, 0)              # Keeping the window from being resized


def btn_click(item):               # This updates the input field whenever any button is pressed
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def btn_equal():                    # This creates an equal button to calculate the expression at hand
    global expression
    result = str(eval(expression))  # 'eval' calculates the string expressions directly
    input_text.set(result)
    expression = ""


def btn_clear():                    # This clears the input field (accomplished by using the "C")
    global expression
    expression = ""
    input_text.set("")



expression = ""
input_text = StringVar()            # 'StringVar()' is used to get the instance of the input field




                                    # Creating the input field framework

input_frame = Frame(popUp, width = 312, bd = 0, highlightbackground = "#E09F33", highlightcolor = "#E09F33")
input_frame.pack(side = TOP)


                                    # Creating input field inside the frame

input_field = Entry(input_frame, font = ('avory', 18, 'bold'), textvariable = input_text, width = 50, bg = "#F9F7F4", justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)        # 'ipady' is an internal padding to increase the height of input field


                                    # Creating a separate frame to incorporate the buttons inside it

frame = Frame(popUp, width = 312, height = 272.5, bg = "#F6F0E6")
frame.pack()



                                    # Using the classic calculator set up

                                    # Creating the first row of the calculator (Clear and Divide)

clear = Button(frame, text = "C", fg = "#E09F33", font=('avory', 9), width = 32, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(frame, text = "/", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)


                                    # Creating the second row (7, 8, 9, and Multiply)

seven = Button(frame, text = "7", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(frame, text = "8", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(frame, text = "9", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(frame, text = "*", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)


                                    # Creating the third row (4, 5, 6, and Subtract)

four = Button(frame, text = "4", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(frame, text = "5", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(frame, text = "6", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(frame, text = "-", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)


                                    # Creating the fourth row (1, 2, 3, and Adding)

one = Button(frame, text = "1", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(frame, text = "2", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(frame, text = "3", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(frame, text = "+", fg = "#E09F33", font=('avory', 9), width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)


                                    # Creating the fifth row (0, Decimal, and Equals)

zero = Button(frame, text = "0", font=('avory', 9), foreground = "#E09F33", width = 21, height = 4, bd = 0, background = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
decimal = Button(frame, text = ".", font=('avory', 9), fg = "#E09F33", width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(frame, text = "=", font=('avory', 9), fg = "#E09F33", width = 10, height = 4, bd = 0, bg = "#FFFFFF", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)


popUp.mainloop()
