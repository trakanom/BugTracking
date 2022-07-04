from tkinter import *
from ..config import errors
class ErrorPage:
    def __init__(self, errortype):
        #Error Window with appropriate message
        self.root = Tk()
        text = Text(self.root)
        text.insert(INSERT,errors[errortype])
        text.pack()
        # print(errors[errortype])
        button = Button(self.root,text="Okay",command=self.confirm)
        button.pack()
    def confirm(self):
        #Button to close window
        self.root.destroy()