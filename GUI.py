import tkinter as tk 
#import tkinter.ttk as ttk 

root = tk.Tk()
root.geometry('300x300')
label = tk.Label(text='Wpisz tekst')
entry_name = tk.Entry()
label.pack()
entry_name.pack()

button = tk.Button(text='Dont use it!', fg='white', bg='black', width=10, height=6)
button.pack()
root.mainloop()