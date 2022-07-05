from tkinter import *
class Window:
    def __init__(self,title):
        self.root = Tk()
        self.title = title
        self.root.title(title)
        self.fields={}
        self.labels={}
        self.buttons={}
    def Add_Field(self,title,column,row,width=None,height=None,columnspan=None,rowspan=None):
        pass
        #Let's make some fields for Entries
    def Create_Window(self):
        #When you're done building the window, use this.
        self.root.mainloop()
    def Add_Button(self,title,column,row,command,width=None,height=None,columnspan=None,rowspan=None):
        pass
    def Get_Fields(self,*args):
        pass
        #Returns a dict populated with the content of all fields referenced
