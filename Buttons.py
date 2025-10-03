from tkinter import*
import Calc_Functions as cf
CF = cf.CalculatorFunctions()
font = 'Helvetica 20 bold italic'
row1 = 1
row2 = 2
row3 = 3
row4 = 4
row5 = 5
row6 = 6
row7 = 7
row8 = 8
def make_buttons(gui, entry_line):
    # finance functions
    n_button = Button(gui, text=str("N"), font=font, fg='black', bg='blue',
                    command=lambda: CF.n_func(entry_line), height=1, width=7)
    n_button.grid(row=row1,column=0)

    ipery_button = Button(gui, text=str("I/Y"), font=font, fg='black', bg='blue',
                        command=lambda: CF.ipery_func(entry_line), height=1, width=7)
    ipery_button.grid(row=row1,column=1)

    pv_button = Button(gui, text=str("PV"), font=font, fg='black', bg='blue',
                        command=lambda: CF.pv_func(entry_line), height=1, width=7)
    pv_button.grid(row=row1,column=2)

    fv_button = Button(gui, text=str("FV"), font=font, fg='black', bg='blue',
                        command=lambda: CF.fv_func(entry_line), height=1, width=7)
    fv_button.grid(row=row1,column=3)

    cpt_button = Button(gui, text=str("CPT"), font=font, fg='black', bg='blue',
                        command=CF.cpt_func, height=1, width=7)
    cpt_button.grid(row=row1,column=4)

    # number buttons
    button1 = Button(gui, text=str(1), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(1, entry_line), height=1, width=7)
    button1.grid(row=row4, column=0)

    button2 = Button(gui, text=str(2), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(2, entry_line), height=1, width=7)
    button2.grid(row=row4, column=1)

    button3 = Button(gui, text=str(3), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(3, entry_line), height=1, width=7)
    button3.grid(row=row4, column=2)

    button4 = Button(gui, text=str(4), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(4, entry_line), height=1, width=7)
    button4.grid(row=row5, column=0)   

    button5 = Button(gui, text=str(5), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(5, entry_line), height=1, width=7)
    button5.grid(row=row5, column=1)

    button6 = Button(gui, text=str(6), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(6, entry_line), height=1, width=7)
    button6.grid(row=row5, column=2)

    button7 = Button(gui, text=str(7), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(7, entry_line), height=1, width=7)
    button7.grid(row=row6, column=0)

    button8 = Button(gui, text=str(8), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(8, entry_line), height=1, width=7)
    button8.grid(row=row6, column=1)

    button9 = Button(gui, text=str(9), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(9, entry_line), height=1, width=7)
    button9.grid(row=row6, column=2)

    button0 = Button(gui, text=str(0), font=font, fg='black', bg='blue',
                    command=lambda: CF.press(0, entry_line), height=1, width=7)
    button0.grid(row=row7, column=0)
    #basic operations
    plus = Button(gui, text=' + ', font=font, fg='black', bg='blue',
                    command=lambda: CF.press('+', entry_line), height=1, width=7)
    plus.grid(row=row3, column=0)

    minus = Button(gui, text=' - ', font=font, fg='black', bg='blue',
                    command=lambda: CF.press('-', entry_line), height=1, width=7)
    minus.grid(row=row3, column=1)

    multiply = Button(gui, text=' * ', font=font, fg='black', bg='blue',
                    command=lambda: CF.press('*', entry_line), height=1, width=7)
    multiply.grid(row=row3, column=2)

    divide = Button(gui, text=' / ', font=font, fg='black', bg='blue',
                    command=lambda: CF.press('/', entry_line), height=1, width=7)
    divide.grid(row=row3, column=3)

    equal = Button(gui, text='=', font=font, fg='black', bg='blue',
                    command=lambda: CF.equal_press(entry_line), height=1, width=7)
    equal.grid(row=row6, column=3)
    #util buttons
    deletebutton = Button(gui, text='del', font=font, fg='black', bg='blue',
                    command=lambda: CF.delete(entry_line), height=1, width=7)
    deletebutton.grid(row=row2, column=0)

    decimalbutton = Button(gui, text=' . ', font=font, fg='black', bg='blue',
                    command=lambda: CF.press('.', entry_line), height=1, width=7)
    decimalbutton.grid(row=row7, column=1)

    clearbutton = Button(gui, text='clear', font=font, fg='black', bg='blue',
                    command=lambda: CF.clear(entry_line), height=1, width=7)
    clearbutton.grid(row=row2, column=1)

    Lbracket = Button(gui, text='(', font=font, fg='black', bg='blue',
                    command=lambda: CF.press('(', entry_line), height=1, width=7)
    Lbracket.grid(row=row4, column=3)

    Rbracket = Button(gui, text=')', font=font, fg='black', bg='blue',
                    command=lambda: CF.press(')', entry_line), height=1, width=7)
    Rbracket.grid(row=row5, column=3)
    #extra math operations
    square_root_button = Button(gui, text='√x', font=font, fg='black', bg='blue',
                    command=lambda: CF.square_root(entry_line), height=1, width=7)
    square_root_button.grid(row=row7, column=2)

    inverse_button = Button(gui, text='1/x', font=font, fg='black', bg='blue',
                    command=lambda: CF.inverse(entry_line), height=1, width=7)
    inverse_button.grid(row=row7, column=3)