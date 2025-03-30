import tkinter as tk
from tkinter.colorchooser import askcolor

def start_drawing(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def draw(event):
    global prev_x, prev_y, brush_color
    canvas.create_line(prev_x, prev_y, event.x, event.y, fill=brush_color, width=2)
    prev_x, prev_y = event.x, event.y

def clear_cavas():
    canvas.delete('all')

def choose_color():
    global brush_color
    color = askcolor(title='Choose Color')
    if color[1]:
        brush_color = color[1]


window = tk.Tk()
window.title('Painting App')

canvas = tk.Canvas(window, bg='white', width=400, height=400)
canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

canvas.bind('<Button-1>', start_drawing)
canvas.bind('<B1-Motion>', draw)

brush_color = 'black'

clear_button = tk.Button(window, text ='Clear', command=clear_cavas)
clear_button.pack(padx=10, pady=10)

choose_color_button = tk.Button(window, text='Choose color', command = choose_color)
choose_color_button.pack(padx=10, pady=10)

window.mainloop()