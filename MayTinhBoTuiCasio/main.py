from tkinter import *

wd = Tk()
wd.title ('Casio Claculator')
def bt_click (number):
    e.insert(END, number)
def addition():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global operator
    operator = 1
def subtraction():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global operator
    operator = 2
def claculation():
    global num1
    global operator
    num2 = int(e.get())
    e.delete(0, END)
    if operator == 1:
        e.insert(END, num1 + num2)
    if operator == 2:
        e.insert(END, num1 - num2)
    if operator == 3:
        e.insert(END, num1 * num2)
    if operator == 4:
        e.insert(END, num1 / num2)
def multiplication():
    global num1
    global num2
    num1 = int(e.get())
    e.delete(0, END)
    global operator
    operator = 3
def division ():
    global num1
    global num2
    num1 = int(e.get())
    e.delete(0, END)
    global operator
    operator = 4
def clear():
    e.delete(0, END)

e = Entry (width=20, borderwidth=5, font='Arial 18', justify=RIGHT)
bt_7 = Button (text='7', width=10, height=3 ,command=lambda: bt_click(7))
bt_8 = Button (text='8', width=10, height=3 , command=lambda: bt_click(8))
bt_9 = Button (text='9', width=10, height=3 ,command=lambda: bt_click(9))
bt_div = Button (text='/', width=10, height=3 ,command=division)
bt_4 = Button (text='4', width=10, height=3 ,command=lambda: bt_click(4))
bt_5 = Button (text='5', width=10, height=3 ,command=lambda: bt_click(5))
bt_6 = Button (text='6', width=10, height=3 ,command=lambda: bt_click(6))
bt_mul = Button (text='*', width=10, height=3 ,command=multiplication)
bt_1 = Button (text='1', width=10, height=3 ,command=lambda: bt_click(1))
bt_2 = Button (text='2', width=10, height=3 ,command=lambda: bt_click(2))
bt_3 = Button (text='3', width=10, height=3 ,command=lambda: bt_click(3))
bt_sub = Button (text='-', width=10, height=3 ,command=subtraction)
bt_0 = Button (text='0', width=10, height=3 ,command=lambda: bt_click(0))
bt_clear = Button (text='Clear', width=10, height=3 ,command=clear)
bt_eq = Button (text='=', width=10, height=3 ,command=claculation)
bt_add = Button (text='+', width=10, height=3 ,command=addition)

e.grid(row=0, column=0, columnspan=4, pady=10)
bt_7.grid(row=1, column=0)
bt_8.grid(row=1, column=1)
bt_9.grid(row=1, column=2)
bt_div.grid(row=1, column=3)
bt_4.grid(row=2, column=0)
bt_5.grid(row=2, column=1)
bt_6.grid(row=2, column=2)
bt_mul.grid(row=2, column=3)
bt_1.grid(row=3, column=0)
bt_2.grid(row=3, column=1)
bt_3.grid(row=3, column=2)
bt_sub.grid(row=3, column=3)
bt_clear.grid(row=4, column=0)
bt_eq.grid(row=4, column=2)
bt_add.grid(row=4, column=3)
wd.mainloop()