from tkinter import *
entry = ''
font = 'Helvetica 20 bold italic'
mem = ''
def square_root():
    global entry
    total = str(eval('(' + entry + ') **  (1/2)'))
    entry_line.set(total)
def inverse():
    global entry
    total = str(eval('1/'+entry))
    entry_line.set(total)
def equal_press():
    try:
        global entry
        total = str(eval(entry))
        entry_line.set(total)
    except:
        entry_line.set('Error')
        entry = ''
def press(num):
    global entry
    entry = entry + str(num)
    entry_line.set(entry)
def clear():
    global entry
    entry = ''
    entry_line.set('')
def delete():
    global entry
    entry = entry[0:-1]
    entry_line.set(entry)
def n_func():
    global entry

def make_buttons():
    n_button = Button(gui, text=str("N"), font=font, fg='black', bg='blue',
                    command=n_func, height=1, width=7)
    n_button.grid(row=1,column=0)

    button1 = Button(gui, text=str(1), font=font, fg='black', bg='blue',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=4, column=0)

    button2 = Button(gui, text=str(2), font=font, fg='black', bg='blue',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=4, column=1)

    button3 = Button(gui, text=str(3), font=font, fg='black', bg='blue',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=4, column=2)

    button4 = Button(gui, text=str(4), font=font, fg='black', bg='blue',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=5, column=0)   

    button5 = Button(gui, text=str(5), font=font, fg='black', bg='blue',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=5, column=1)

    button6 = Button(gui, text=str(6), font=font, fg='black', bg='blue',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=5, column=2)

    button7 = Button(gui, text=str(7), font=font, fg='black', bg='blue',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=6, column=0)

    button8 = Button(gui, text=str(8), font=font, fg='black', bg='blue',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=6, column=1)

    button9 = Button(gui, text=str(9), font=font, fg='black', bg='blue',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=6, column=2)

    button0 = Button(gui, text=str(0), font=font, fg='black', bg='blue',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=7, column=0)

    plus = Button(gui, text=' + ', font=font, fg='black', bg='blue',
                    command=lambda: press('+'), height=1, width=7)
    plus.grid(row=3, column=0)

    minus = Button(gui, text=' - ', font=font, fg='black', bg='blue',
                    command=lambda: press('-'), height=1, width=7)
    minus.grid(row=3, column=1)

    multiply = Button(gui, text=' * ', font=font, fg='black', bg='blue',
                    command=lambda: press('*'), height=1, width=7)
    multiply.grid(row=3, column=2)

    divide = Button(gui, text=' / ', font=font, fg='black', bg='blue',
                    command=lambda: press('/'), height=1, width=7)
    divide.grid(row=3, column=3)

    deletebutton = Button(gui, text='del', font=font, fg='black', bg='blue',
                    command=delete, height=1, width=7)
    deletebutton.grid(row=2, column=0)

    decimalbutton = Button(gui, text=' . ', font=font, fg='black', bg='blue',
                    command=lambda: press('.'), height=1, width=7)
    decimalbutton.grid(row=7, column=1)

    equal = Button(gui, text='=', font=font, fg='black', bg='blue',
                    command=equal_press, height=1, width=7)
    equal.grid(row=6, column=3)

    clearbutton = Button(gui, text='clear', font=font, fg='black', bg='blue',
                    command=clear, height=1, width=7)
    clearbutton.grid(row=2, column=1)

    Lbracket = Button(gui, text='(', font=font, fg='black', bg='blue',
                    command=lambda: press('('), height=1, width=7)
    Lbracket.grid(row=4, column=3)

    Rbracket = Button(gui, text=')', font=font, fg='black', bg='blue',
                    command=lambda: press(')'), height=1, width=7)
    Rbracket.grid(row=5, column=3)

    square_root_button = Button(gui, text='√x', font=font, fg='black', bg='blue',
                    command=square_root, height=1, width=7)
    square_root_button.grid(row=7, column=2)

    inverse_button = Button(gui, text='1/x', font=font, fg='black', bg='blue',
                    command=inverse, height=1, width=7)
    inverse_button.grid(row=7, column=3)


gui = Tk()
gui.configure(background='gray')
gui.title("Colin's Calculator")
gui.geometry("800x500")
entry_line = StringVar()
expression_field = Entry(gui, textvariable=entry_line, font=font)
expression_field.grid(row=0, columnspan=5, ipadx=100)
make_buttons()
gui.mainloop()
