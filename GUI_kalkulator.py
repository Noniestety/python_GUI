import tkinter as tk 
from math import sqrt

def button_click_func(entry):
    current = calulator_screen.get()
    calulator_screen.delete(0, tk.END)
    calulator_screen.insert(tk.END, current + str(entry))

def button_clear_func():
    calulator_screen.delete(0, tk.END)

def button_equal_func():
    expression = calulator_screen.get()
    try:
        result = eval(expression)
        calulator_screen.delete(0,tk.END)
        calulator_screen.insert(tk.END, result)
    except Exception as ex:
        calulator_screen.delete(0,tk.END)
        calulator_screen.insert(tk.END, 'Error')

#main window
window = tk.Tk()
window.title('Calculator')

#field to display results
calulator_screen = tk.Entry(master=window)
calulator_screen.grid(row=0, column=0, columnspan= 4, padx=10, pady=10, sticky='nsew')
# row i column, okreslami wierszi kolumne gdzie startujemy
# columnspan - na ile kolumn zostanie rozciagniety
# padx i y okresla ile bedzie przestrzeni miedzy krawedziami widgeru a krawedziamy okna
#sticky - okresla do ktorej krawedzi bedzie przylegac n-north itd, nsew - wszystkie kierunk, rozciaga sie w kazda strone

#Buttons settings
padx = 20
pady = 10
#Create number buttons
button_1 = tk.Button(window, text='1', padx=padx, pady=pady, command=lambda: button_click_func(1))
button_2 = tk.Button(window, text='2', padx=padx, pady=pady, command=lambda: button_click_func(2))
button_3 = tk.Button(window, text='3', padx=padx, pady=pady, command=lambda: button_click_func(3))
button_4 = tk.Button(window, text='4', padx=padx, pady=pady, command=lambda: button_click_func(4))
button_5 = tk.Button(window, text='5', padx=padx, pady=pady, command=lambda: button_click_func(5))
button_6 = tk.Button(window, text='6', padx=padx, pady=pady, command=lambda: button_click_func(6))
button_7 = tk.Button(window, text='7', padx=padx, pady=pady, command=lambda: button_click_func(7))
button_8 = tk.Button(window, text='8', padx=padx, pady=pady, command=lambda: button_click_func(8))
button_9 = tk.Button(window, text='9', padx=padx, pady=pady, command=lambda: button_click_func(9))
button_0 = tk.Button(window, text='0', padx=padx, pady=pady, command=lambda: button_click_func(0))
#operator buttons
button_add = tk.Button(window, text='+', padx=padx, pady=pady, command=lambda: button_click_func('+'))
button_subtract = tk.Button(window, text='-', padx=padx, pady=pady, command=lambda: button_click_func('-'))
button_multiply = tk.Button(window, text='*', padx=padx, pady=pady, command=lambda: button_click_func('*'))
button_divide = tk.Button(window, text='/', padx=padx, pady=pady, command=lambda: button_click_func('/'))
button_equal = tk.Button(window, text='=', padx=padx, pady=pady, command= button_equal_func)
button_clear = tk.Button(window, text='C', padx=padx, pady=pady, command = button_clear_func)

button_power_two = tk.Button(window, text='^', padx=padx, pady=pady, command=lambda: button_click_func('**') )
button_sqrt = tk.Button(window, text='√', padx=padx, pady=pady, command=lambda: button_click_func('sqrt'))
button_left_bracket = tk.Button(window, text='(', padx=padx, pady=pady, command=lambda: button_click_func('(') )
button_right_bracket = tk.Button(window, text=')', padx=padx, pady=pady, command=lambda: button_click_func(')'))


# Ustawianie guzików na siatce
sticky = 'nsew'

button_7.grid(row=1, column= 0, sticky=sticky)
button_8.grid(row=1, column= 1, sticky=sticky)
button_9.grid(row=1, column= 2, sticky=sticky)
button_add.grid(row=1, column= 3, sticky=sticky)

button_4.grid(row=2, column= 0, sticky=sticky)
button_5.grid(row=2, column= 1, sticky=sticky)
button_6.grid(row=2, column= 2, sticky=sticky)
button_subtract.grid(row=2, column= 3, sticky=sticky)

button_1.grid(row=3, column= 0, sticky=sticky)
button_2.grid(row=3, column= 1, sticky=sticky)
button_3.grid(row=3, column= 2, sticky=sticky)
button_multiply.grid(row=3, column= 3, sticky=sticky)

button_0.grid(row=4, column= 0, sticky=sticky)
button_clear.grid(row=4, column= 1, sticky=sticky)
button_equal.grid(row=4, column= 2, sticky=sticky)
button_divide.grid(row=4, column= 3, sticky=sticky)

button_power_two.grid(row=5, column= 0, sticky=sticky)
button_sqrt.grid(row=5, column= 1, sticky=sticky)
button_left_bracket.grid(row=5, column= 2, sticky=sticky)
button_right_bracket.grid(row=5, column= 3, sticky=sticky)

window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=1)
window.grid_columnconfigure(3,weight=1)



window.grid_rowconfigure(0,weight=1)

window.mainloop()