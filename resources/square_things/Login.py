# from ...resources.configurator import MasterList
from tkinter import *
from ..classes.Windows import Window
from .Error import ErrorPage
class Login:
    def __init__(self,Userlist):
        self.Userlist = Userlist

    def Log_In(self):
        #Compare entered information to database
        #If match, destroy window, open landing page
        # try:
        user = self.root.fields["Username"].get()
        #replace this with auth stuff
        if (user in self.Userlist.TheList.keys()) and (self.Userlist.TheList[user].PW_Hash == self.root.fields["Password"].get()):
            from .Landing import Landing_Page
            print("We're in.")
            self.root.Close_Window()
            Landing = Landing_Page(self.Userlist,user)
            Landing.Open_Window()
        else:
            ErrorPage("Incorrect Information")
        # except:
            # ErrorPage("Missing Field")
    def Edit_Users(self):
        
        user = self.root.fields["Username"].get()
        #replace this with auth stuff
        if (user in self.Userlist.TheList.keys()) and (self.Userlist.TheList[user].PW_Hash == self.root.fields["Password"].get()):
            from .Edit_User import Edit_Users
            print("We're in.")
            self.root.Close_Window()
            EditUsers = Edit_Users(self.Userlist,user)
            EditUsers.Open_Window()
        else:
            ErrorPage("Incorrect Information")
    def Open_Window(self):
        #Initialize window with fields for username & password, and buttons for logging in and editing users
        self.root = Tk()
        self.root.title("Log In")
        self.username = Entry(self.root, width=30)
        self.password = Entry(self.root,width=30)
        self.username.grid(column=0,row=0,columnspan=2)
        self.password.grid(column=0,row=1,columnspan=2)
        Button(self.root, text="Log In", command=self.Log_In).grid(column=3, row=0, columnspan=1)
        Button(self.root, text="Edit User", command=self.Edit_Users).grid(column=3, row=1, columnspan=1)
        self.root.mainloop()
    def New_Open_Window(self):
        self.root = Window("Login")
        self.root.Add_Field("Username",0,0,45,8,2)
        self.root.Add_Field("Password",0,1,45,8,2)
        self.root.Add_Button("Log In",6,0,self.Log_In,10,8,1)
        self.root.Add_Button("Edit User",6,1,self.Edit_Users,10,8,1)
        self.root.Create_Window()
    def Login_Error(self,errortype):
        ErrorPage(errortype)