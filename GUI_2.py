import tkinter as tk 
#import tkinter.ttk as ttk 

root = tk.Tk()

frame1=tk.Frame(master=root, width=150, height=150, bg='black')
frame1.pack(side=tk.LEFT)

frame2=tk.Frame(master=root, width=100, height=100, bg='blue')
frame2.pack()

frame3=tk.Frame(master=root, width=50, height=50, bg='red')
frame3.pack(fill=tk.X)

root.mainloop()