# -*- encoding:utf-8 -*-
import sys, os, math

from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import askyesno
from PIL import Image
from PIL.ImageTk import PhotoImage


Version = '1.00'

#############################################
# 主体框架
#############################################

class MyPhotoMainFrame():
    menus = []
    dir_path = ''
    thumbs_save = []
    onView_save = []

    def __init__(self):
        self.main = Tk()
        self.main.title('MyPhoto' + Version)
        self.makeMenu()
        self.canv_main = makeScrolledCanvas(self.main)
        self.makeFrame()

#############################################
# 菜单栏
#############################################

    def makeMenu(self):
        self.start()
        menubar = Menu(self.main)
        self.main.config(menu=menubar)
        if sys.platform[:3] == 'win':
            for (name, key, cmd) in self.menus:
                menubar.add_command(label=name, underline=key, command=cmd)
        else:
            for (name, key, cmd) in self.menus:
                pulldown = Menu(menubar)
                pulldown.add_command(label=name, underline=key, command=cmd)
                menubar.add_cascade(label=name, menu=pulldown, underline=key)

    def onOpen(self):
        self.dir_path = askdirectory(initialdir='/')
        if self.dir_path:
            self.thumbs_save = []
            self.canv_main.delete(self.canv_main_win)
            self.makeFrame()

    def onClose(self):
        self.dir_path = ''
        self.canv_main.delete(self.canv_main_win)
        self.makeFrame()

    def onQuit(self):
        if askyesno('MyPhoto', 'Sure to quit?'):
            sys.exit()

#############################################
# 主体框架
#############################################

    def makeFrame(self, cols=None):
        frame = Frame(self.canv_main)
        frame.pack(side=TOP, fill=BOTH, expand=YES)
        if self.dir_path:
            img_obj = self.makeThumbs()
            filenum = len(img_obj)
            cols = cols or math.trunc(math.sqrt(filenum))
            row = 0
            while img_obj:
                column = 0
                img_row, img_obj = img_obj[:cols], img_obj[cols:]
                for (file, img) in img_row:
                    btn_img = PhotoImage(img)
                    btn = Button(frame, image=btn_img, width=128, height=128,
                                 command=lambda file=file: OnView(self.main, file, self.dir_path))
                    btn.grid(row=row, column=column)
                    column += 1
                    self.thumbs_save.append(btn_img)
                row += 1
            x_scrollregion = row * 128
            y_scrollregion = (cols + 2) * 128
            self.canv_main.config(scrollregion=(0, 0, x_scrollregion, y_scrollregion))
            self.canv_main_win = self.canv_main.create_window(0, 0, anchor=NW, window=frame)
        else:
            Label(frame, text='Please select an image directory...', height=10,
                  width=50).pack(side=TOP, fill=BOTH)
            self.canv_main_win = self.canv_main.create_window(360, 240, window=frame)



#############################################
# 功能调用
#############################################

    def makeThumbs(self, size=(128, 128)):
        files = os.listdir(self.dir_path)
        dir_path = self.dir_path
        thumb_path = os.path.join(dir_path, 'thumbs')
        img_obj = []
        if not os.path.exists(thumb_path):
            os.mkdir(thumb_path)
        for file in files:
            if not os.path.exists(os.path.join(thumb_path, file)):
                try:
                    img = Image.open(os.path.join(dir_path, file))
                    img.thumbnail(size, Image.ANTIALIAS)
                    img.save(os.path.join(thumb_path, file))
                    print('Creating thumbs => %s' % file)
                except:
                    print('Skipfile => %s' % file)
                else:
                    img_obj.append((file, img))
            else:
                img = Image.open(os.path.join(thumb_path, file))
                img_obj.append((file, img))
                print('Exist thumbs => %s' %file)
        return img_obj

    def start(self):
        self.menus = [('Open', 0, self.onOpen),
                 ('Close', 0, self.onClose),
                 ('Quit', 0, self.onQuit)]


####################################################
# 图片查看窗口, 尝试在threading中运行图片缩放以免阻塞GUI
####################################################

import threading, queue, decimal


class OnView(Toplevel):
    onView_save = ['img', 'img_obj', 'resize_img']
    if sys.platform[:3] == 'win':
        scale = 1200
    else:
        scale = 10
    zoom_scale = 0
    data = queue.Queue()

    def __init__(self, parent, file, dir_path):
        Toplevel.__init__(self, parent)
        self.title('MyPhoto - %s' % file)
        self.canv = makeScrolledCanvas(self)
        img_path = os.path.join(dir_path, file)
        self.img = Image.open(img_path)
        self.onView_save[0] = self.img
        img_obj = PhotoImage(self.img)
        if self.img.size[0] < 720:
            self.canv.config(width=self.img.size[0])
        if self.img.size[1] < 480:
            self.canv.config(height=self.img.size[1])
        self.canv.config(scrollregion=(0, 0, self.img.size[0], self.img.size[1]))
        self.canv_img = self.canv.create_image(0, 0, anchor=NW, image=img_obj)
        self.onView_save[1] = img_obj
        self.canv.bind('<MouseWheel>', self.onMouseZoom)

    def onMouseZoom(self, event):
        zoom = decimal.Decimal(event.delta) / decimal.Decimal(self.scale)
        if -0.8 <= self.zoom_scale + zoom <= 2:
            self.zoom_scale += zoom
        else:
            return
        origin = self.img.size
        size = int(origin[0] * (1 + self.zoom_scale)), int(origin[1] * (1 + self.zoom_scale))
        threading.Thread(group=None, target=self.zoomer, args=(size,)).start()
        self.displayer()

    def zoomer(self, size):
        img = self.img.resize(size, Image.ANTIALIAS)
        img_obj = PhotoImage(img)
        self.onView_save[1], self.onView_save[2] = img_obj, img
        self.data.put((img, img_obj), block=False)

    def displayer(self):
        try:
            img, img_obj = self.data.get(block=False)
        except queue.Empty:
            pass
        else:
            self.canv_img = self.canv.create_image(0, 0, anchor=NW, image=img_obj)
            self.canv.config(scrollregion=(0, 0, img.size[0], img.size[1]))
            self.canv.update()
        finally:
            self.canv.after(100, self.displayer)

def makeScrolledCanvas(parent):
    frame = Frame(parent)
    frame.pack(side=TOP, expand=YES, fill=BOTH)
    yscroll = Scrollbar(frame)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    canvas = Canvas(frame, width=720, height=480,
                    yscrollcommand=yscroll.set,
                    xscrollcommand=xscroll.set)
    yscroll.config(command=canvas.yview, relief=FLAT)
    xscroll.config(command=canvas.xview, relief=FLAT)
    yscroll.pack(side=RIGHT, fill=Y)
    xscroll.pack(side=BOTTOM, fill=X)
    canvas.pack(side=TOP, fill=BOTH, expand=YES)
    return canvas


if __name__ == '__main__':
    class Test(MyPhotoMainFrame):
        def onOpen(self):
            self.dir_path = askdirectory(initialdir='/Users/joshuapu/Documents/wallpaper')
            if self.dir_path:
                self.thumbs_save = []
                self.canv_main.delete(self.canv_main_win)
                self.makeFrame()

    Test()
    mainloop()