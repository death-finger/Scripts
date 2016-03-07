# e.g. 8-46
import os, sys
from tkinter import *
import viewer_thumbs
from PIL import Image


def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    thumbs = []
    for imgfile in os.listdir(imgdir):
        imgpath = os.path.join(imgdir, imgfile)
        try:
            imgobj = Image.open(imgpath)
            imgobj.thumbnail(size)
            thumbs.append((imgfile, imgobj))
        except:
            print('Skipping', imgpath)
    return thumbs

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'images'
    viewer_thumbs.makeThumbs = makeThumbs
    main, save = viewer_thumbs.viewer(imgdir, kind=Tk)
    main.mainloop()