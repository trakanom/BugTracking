from tkinter import *

from resources.classes.Userlists import UserList
class Landing_Page:
    def __init__(self,Userlist,username):
        self.username = username
        self.Userlist = Userlist
        pass
    def Add_Project(self):
        #Opens the Edit_Project window with blank fields.
        #After "Save_Project" function is used, adds project to database of projects after checking for an existing match.
        pass
    def Edit_Project(self):
        from .Edit_Project import Project_Window
        project = Project_Window(self.Userlist,self.username,None)
        project.Open_Window()
        #Opens the Edit_Project window with pre-filled fields based on the info already in the database
        pass
    def View_Project(self):
        #Opens the Project_Overview window.
        pass
    def Open_Settings(self):
        #Opens the Settings window
        pass
    def Logoff(self):
        #Close window
        #Open Login window
        self.root.destroy()
        from .Login import Login
        newlogin = Login(self.Userlist)
        newlogin.OpenWindow()
        #Closes the Landing_Page window and returns to Login window
    def Open_Window(self):
        #Initialize window
        self.root = Tk()
        Button(self.root, text="Add Project", command=self.Add_Project).grid(column=0, row=0, columnspan=2)
        Button(self.root, text="Edit Project", command=self.Edit_Project).grid(column=0, row=1, columnspan=2)
        Button(self.root, text="View Project", command=self.View_Project).grid(column=0, row=2, columnspan=2)
        Button(self.root, text="Settings", command=self.Open_Settings).grid(column=0, row=5, columnspan=2)
        Button(self.root, text="Log Off", command=self.Logoff).grid(column=0, row=6, columnspan=2)
        self.root.mainloop()