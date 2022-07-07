from tkinter import *
from ..config import errors
from ..classes.Windows import Window
class ErrorPage:
    def __init__(self, errortype):
        #Error Window with appropriate message
        self.root = Tk()
        text = Label(self.root,text=errors[errortype]).grid(column=0,row=0,columnspan=3)
        # text.insert(INSERT,errors[errortype])
        # text.pack()
        # print(errors[errortype])
        button = Button(self.root,text="Okay",command=self.confirm).grid(column=1,row=1)
        # button.pack()
    def confirm(self):
        #Button to close window
        self.root.destroy()
    def Old_Init(self,errortype):
    #Error Window with appropriate message
        self.root = Tk()
        text = Text(self.root)
        text.insert(INSERT,errors[errortype])
        text.pack()
        # print(errors[errortype])
        button = Button(self.root,text="Okay",command=self.confirm)
        button.pack()