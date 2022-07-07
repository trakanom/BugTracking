from tkinter import *
class Window:
    def __init__(self,title,*args):
        self.root = Tk()
        self.title = title
        self.root.title(title)
        self.fields={}
        self.labels={}
        self.buttons={}
        self.args = {arg for arg in args}
    def Add_Field(self,title,column,row,width=None,height=None,columnspan=None,rowspan=None,default_value=None):
        #Let's make some fields for Entries
        columnspan=1 if columnspan == None else columnspan
        rowspan=1 if rowspan == None else rowspan
        width=30 if width == None else width
        height=8 if height == None else height
        self.fields[title]=Entry(self.root,width=width)
        if default_value != None:
            self.fields[title].insert(0,default_value)
        self.labels[title]=Label(self.root,text=(title+':')).grid(column=column,row=row)
        self.fields[title].grid(column=(column+1),row=row,columnspan=columnspan,rowspan=rowspan)
    def Create_Window(self):
        #When you're done building the window, use this.
        self.root.mainloop()
    def Add_Button(self,title,column,row,command,width=None,height=None,columnspan=None,rowspan=None):
        columnspan=1 if columnspan == None else columnspan
        rowspan=1 if rowspan == None else rowspan
        width=30 if width == None else width
        height=8 if columnspan == None else columnspan
        self.buttons[title]=Button(self.root,text=title,command=command,width=width,height=height).grid(column=column,row=row,columnspan=columnspan,rowspan=rowspan)
    def Get_Fields(self,*args):
        #Returns a dict populated with the content of all fields referenced
        #Usage:
        #newWindow.Add_Button("Test Fields",2,3,lambda: newWindow.Get_Fields("Test Field 1","Test Field 2"))
        return {str(arg):self.fields[arg].get() for arg in args}
        #Todo: Figure out how to avoid errors.
    def Close_Window(self):
        #Closes window
        self.root.destroy()
    def Add_Dropdown(self,title,contents,column,row,default_text=None):
            self.fields[title] = StringVar(self.root) #define our variable
            self.fields[title].set(default_text) #default
            self.labels[title]=Label(self.root,text=(title+":")).grid(column=column,row=row)
            w=OptionMenu(self.root,self.fields[title],*contents)
            w.grid(column=(column+1),row=row)
        
        
#Usage Notes:
# newWindow=Window("NEW TEST WINDOW")
# newWindow.Add_Field("Test Field 1",0,0,30,8,1,1)
# newWindow.Add_Field("Test Field 2",0,1,30,8,1,1)
# newWindow.Add_Field("Test Field 3",2,0,30,8,1,1)
# newWindow.Add_Field("Test Field 4",2,1,30,8,1,1)
# newWindow.Add_Button("Test Button",0,3,newWindow.root.destroy)
# # wtf = newWindow.Get_Fields("Test Field 1","Test Field 3")
# newWindow.Add_Button("Test Fields",2,3,lambda: newWindow.Get_Fields("Test Field 1","Test Field 2"))
# newWindow.Add_Button("Maparoonie",3,3,lambda:print(list(map(lambda x: newWindow.Get_Fields(x),newWindow.fields.keys()))))
# newWindow.Create_Window()
