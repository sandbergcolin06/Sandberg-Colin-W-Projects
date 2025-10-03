import Buttons as b
##import Calc_Functions as cf
from tkinter import *
#Driver Code
gui = Tk()
##CalcFunc = CalculatorFunctions()
gui.configure(background='gray')
gui.title("Colin's Calculator")
gui.geometry("800x500")
entry_line = StringVar()
expression_field = Entry(gui, textvariable=entry_line, font=b.font)
expression_field.grid(row=0, columnspan=5, ipadx=100)
b.make_buttons(gui, entry_line)
gui.mainloop()
