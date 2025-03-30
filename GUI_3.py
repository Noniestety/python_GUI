import tkinter as tk 
#import tkinter.ttk as ttk 

root = tk.Tk()
root.geometry('300x300')

def click():
    print('Thanks!')

button = tk.Button(text='Click me!', command=click)
button.pack(expand=True)
root.mainloop()