# e.g. 11-6

import os
from tkinter import *
from PP4E.GUI.TextEditor.textEditor import *
from slideShow import SlideShow
Size = (300, 550)


class SlideShowPlus(SlideShow):
    def __init__(self, parent, picdir, editclass, msecs=2000, size=Size):
        self.msecs = msecs
        self.editclass = editclass
        SlideShow.__init__(self, parent, picdir, msecs, size)

    def makeWidgets(self):
        self.name = Label(self, text='None', bg='red', relief=RIDGE)
        self.name.pack(fill=X)
        SlideShow.makeWidgets(self)
        Button(self, text='Note', command=self.onNote).pack(fill=X)
        Button(self, text='Help', command=self.onHelp).pack(fill=X)
        s = Scale(label='Speed: msec delay', command=self.onScale,
                  from_=0, to=3000, resolution=50, showvalue=YES,
                  length=400, tickinterval=250, orient=HORIZONTAL)
        s.pack(side=BOTTOM, fill=X)
        s.set(self.msecs)

        self.editorGone = False
        class WrapEditor(self.editclass):
            def onQuit(editor):
                self.editorGone = True
                self.editorUp = False
                self.editclass.onQuit(editor)

        if issubclass(WrapEditor, TextEditorMain):
            self.editor = WrapEditor(self.master)
        else:
            self.editor = WrapEditor(self)
        self.editor.pack_forget()
        self.editorUp = self.image = None

    def onStart(self):
        SlideShow.onStop(self)
        self.config(cursor='watch')

    def onStop(self):
        SlideShow.onStop(self)
        self.config(cursor='hand2')

    def quit(self):
        self.saveNote()
        SlideShow.quit(self)

    def drawNext(self):
        SlideShow.drawNext(self)
        if self.image:
            self.name.config(text=os.path.split(self.image[0])[1])
        self.loadNote()

    def onScale(self, value):
        self.msecs = int(value)

    def onNote(self):
        if self.editorGone:
            return
        if self.editorUp():
            self.editor.pack_forget()
            self.editorUp = False
        else:
            self.editor.pack(side=TOP, expand=YES, fill=BOTH)
            self.editorUp = True
            self.update()
            self.loadNote()

    def switchNote(self):
        if self.editorUp:
            self.saveNote()
            self.loadNote()

    def saveNote(self):
        if self.editorUp:
            currfile = self.editor.getFileName()
            currtext = self.editor.getAllText()
            if currfile and currtext:
                try:
                    open(currfile, 'w').write(currtext)
                except:
                    pass

    def loadNote(self):
        if self.image and self.editorUp:
            root, ext = os.path.splitext(self.image[0])
            notefile = root + '.note'
            self.editor.setFileName(notefile)
            try:
                self.editor.setAllText(open(notefile).read())
            except:
                self.editor.clearAllText()

    def onHelp(self):
        showinfo('About PyView',
                 'PyView Version 1.2\nMay, 2010\n(1.1 July 1999)\n'
                 'An image slide show\nProgramming Python 4E')


if __name__ == '__main__':
    import sys
    picdir = '../gifs'
    if len(sys.argv) >= 2:
        picdir = sys.argv[1]

    editstyle = TextEditorComponentMinimal
    if len(sys.argv) == 3:
        try:
            editstyle = [TextEditorMain,
                         TextEditorMainPopup,
                         TextEditorComponent,
                         TextEditorComponentMinimal][int(sys.argv[2])]
        except:
            pass

    root = Tk()
    root.title('PyView 1.2 - plus text notes')
    Label(root, text='Slide show subclass').pack()
    SlideShowPlus(parent=root, picdir=picdir, editclass=editstyle)
    root.mainloop()