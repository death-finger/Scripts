from PIL import Image
from PIL.ImageTk import PhotoImage

file = Image.open('1.png', 'r')
out = file.resize((1486, 896), Image.ANTIALIAS)
out.save('2.png')
