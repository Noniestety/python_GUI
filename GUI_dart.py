import tkinter as tk 
from tkinter import scrolledtext
#dodaje kom
#ta funkcja wprowadza wartość rzuconych punktów za pomocą przycisków
def insert_score_func(score):
    player_score.insert(tk.END,  str(score))
# funkcja czyści wartość rzuconych punktów
def button_clear_func():
    player_score.delete(0, tk.END)
# funkcja za pisuje historię rzutow wraz z parametrami kolejki
def player_1_score_save():
    obj_player_score = player_score.get()
    target = rest() 
    remain_score = int(target) - int(obj_player_score)
    player_1_history.config(state='normal')
    player_1_history.insert(tk.END, 'Rzuciłeś ')
    player_1_history.insert(tk.END, str(obj_player_score))
    player_1_history.insert(tk.END, ', ilość lotek: ')
    a = how_many_checkboxes()
    player_1_history.insert(tk.END, a)
    player_1_history.insert(tk.END, ' pozostało: ')
    player_1_history.insert(tk.END,  str(remain_score) + "\n")
    player_1_history.config(state='disabled')
    player_score.delete(0, tk.END)
    
# funkcja która zwraca initail target lub target zredukowany o liczbę punków
def rest():
    last_line_index = player_1_history.index('end-1c').split('.')[0]
    last_line = int(last_line_index) - 1
    obj = player_1_history.get(f'{last_line}.39', f'{last_line}.end')
    if obj == '':
        x = choose_initial_target()
        return x
    else:
        return obj
    
# funkcja sprawdza ile checkboxów jest zaznaczonych
def how_many_checkboxes():
    a=0
    if checkbox_1.get():
        a+=1
    if checkbox_2.get():
        a+=1
    if checkbox_3.get():
        a+=1
    return a   

#wybiera poczatkowy wynik do uzyskania 
def choose_initial_target(): 
    selected_target = radio_button.get()
    return selected_target

#main window
window = tk.Tk()
window.title('Dart Score')
window.configure(bg='yellow')
window.geometry("800x500")

#definicja okien historii graczy
player_1_history = tk.Text(master=window)
player_1_history.grid(row=0, column=0, rowspan= 10, columnspan= 2, padx=10, pady=10, sticky='nsew')

#player_2_history = scrolledtext.ScrolledText(window, width = 4, height = 10, wrap = tk.WORD )
#player_2_history.grid(row=0, column=2, rowspan=10, columnspan= 2, padx=10, pady=10, sticky='nsew')

#definicja okna do wpisywania wyniku
player_score = tk.Entry(master=window)
player_score.grid(row=11, column=0, rowspan=1, columnspan= 2, padx=10, pady=10, sticky='nsew')
label = tk.Label(player_score)
label.configure(text = 'Wprowadz wynik')
label.pack(pady=(0,10))

padx = 20
pady = 10
#definicja guzików
button_1 = tk.Button(window, text='1', padx=padx, pady=pady, command=lambda: insert_score_func(1))
button_2 = tk.Button(window, text='2', padx=padx, pady=pady, command=lambda: insert_score_func(2))
button_3 = tk.Button(window, text='3', padx=padx, pady=pady, command=lambda: insert_score_func(3))
button_4 = tk.Button(window, text='4', padx=padx, pady=pady, command=lambda: insert_score_func(4))
button_5 = tk.Button(window, text='5', padx=padx, pady=pady, command=lambda: insert_score_func(5))
button_6 = tk.Button(window, text='6', padx=padx, pady=pady, command=lambda: insert_score_func(6))
button_7 = tk.Button(window, text='7', padx=padx, pady=pady, command=lambda: insert_score_func(7))
button_8 = tk.Button(window, text='8', padx=padx, pady=pady, command=lambda: insert_score_func(8))
button_9 = tk.Button(window, text='9', padx=padx, pady=pady, command=lambda: insert_score_func(9))
button_0 = tk.Button(window, text='0', padx=padx, pady=pady, command=lambda: insert_score_func(0))
button_player_1_score = tk.Button(window, text='Player 1 score', padx=padx, pady=pady, background='red', command= player_1_score_save)
button_player_2_score = tk.Button(window, text='Player 2 score', padx=padx, pady=pady, bg='blue')
button_clear = tk.Button(window, text='C', padx=padx, pady=pady, command=button_clear_func)

#checkboxy
checkbox_1 = tk.IntVar()
checkbox_2 = tk.IntVar()
checkbox_3 = tk.IntVar()
dart_1 = tk.Checkbutton(window, text='Dart1', variable=checkbox_1)
dart_1.select() # będzie od razu zaznaczony 'deselect' powoduje ze jest odznaczony
dart_2 = tk.Checkbutton(window, text='Dart2', variable=checkbox_2)
dart_2.select() # będzie od razu zaznaczony 'deselect' powoduje ze jest odznaczony
dart_3 = tk.Checkbutton(window, text='Dart3', variable=checkbox_3)
dart_3.select() # będzie od razu zaznaczony 'deselect' powoduje ze jest odznaczony

#radio buttony
radio_button = tk.IntVar()
radio_button_101 = tk.Radiobutton(window, text = '101', variable=radio_button, value= 101)
radio_button_301 = tk.Radiobutton(window, text = '301', variable=radio_button, value= 301)
radio_button_501 = tk.Radiobutton(window, text = '501', variable=radio_button, value= 501)

# Ustawianie guzików na siatce
sticky = 'nsew'
button_1.grid(row=12, column= 0, sticky=sticky)
button_2.grid(row=12, column= 1, sticky=sticky)
button_3.grid(row=12, column= 2, sticky=sticky)
button_4.grid(row=12, column= 3, sticky=sticky)
button_5.grid(row=13, column= 0, sticky=sticky)
button_6.grid(row=13, column= 1, sticky=sticky)
button_7.grid(row=13, column= 2, sticky=sticky)
button_8.grid(row=13, column= 3, sticky=sticky)
button_9.grid(row=14, column= 0, sticky=sticky)
button_0.grid(row=14, column= 1, sticky=sticky)
button_player_1_score.grid(row=14, column= 2, sticky=sticky)
button_player_2_score.grid(row=14, column= 3, sticky=sticky)
button_clear.grid(row=15, column= 0, sticky=sticky)
dart_1.grid(row=15, column= 0, sticky=sticky)
dart_2.grid(row=15, column= 1, sticky=sticky)
dart_3.grid(row=15, column= 2, sticky=sticky)
radio_button_101.grid(row=16, column= 0, sticky=sticky)
radio_button_301.grid(row=16, column= 1, sticky=sticky)
radio_button_501.grid(row=16, column= 2, sticky=sticky)


#definicja kolumn
window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=1)
window.grid_columnconfigure(3,weight=1)
#definicja wierszy
window.grid_rowconfigure(0,weight=1)
# główna pętla
window.mainloop()
