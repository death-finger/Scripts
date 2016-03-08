# e.g. 9-13

from tkinter import *


canvas = Canvas(width=525, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_line(100, 100, 200, 200)
canvas.create_line(100, 200, 200, 300)
for i in range(1, 20, 2):
    canvas.create_line(0, i, 50, i)
canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')
canvas.create_arc(200, 200, 300, 300, width=5, fill='red')
canvas.create_rectangle(0, 300, 150, 150, width=10, fill='green')

photo = PhotoImage(file='../gifs/ora-lp4e.gif')
canvas.create_image(325, 25, image=photo, anchor=NW)

widget = Label(canvas, text='Spam', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)
canvas.create_text(100, 280, text='Ham')
mainloop()
