# e.g. 8-2


from tkinter import *

widget = Button(text='Spam', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(bg='black', fg='white')
widget.config(font=('times', 25, 'italic underline'))
widget.config(bd=8, relief='raised')
widget.config(cursor='target')
mainloop()
