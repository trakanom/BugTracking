# from ...resources.configurator import MasterList
from tkinter import *


class Login:
    def __init__(self,Userlist):
        self.Userlist = Userlist

    def Log_In(self):
        #Compare entered information to database
        #If match, destroy window, open landing page
        try:
            user = self.username.get()
            if self.Userlist.TheList[user].PW_Hash == self.password.get():
                from .Landing import Landing_Page
                print("We're in.")
                self.root.destroy()
                Landing = Landing_Page(self.Userlist,user)
                Landing.Open_Window()
            else:
                from .Error import ErrorPage
                print('Error("Incorrect Information")')
                self.Error = ErrorPage("Incorrect Information")
        except:
            from .Error import ErrorPage
            print('Error("Incorrect Information")')
            self.Error = ErrorPage("Incorrect Information")
        pass

    def OpenWindow(self):
        #Initialize window with fields for username & password, and buttons for logging in and editing users
        self.root = Tk()
        self.root.title("Log In")
        self.username = Entry(self.root, width=30)
        self.password = Entry(self.root,width=30)
        self.username.grid(column=0,row=0,columnspan=2)
        self.password.grid(column=0,row=1,columnspan=2)
        Button(self.root, text="Log In", command=self.Log_In).grid(column=3, row=0, columnspan=1)
        Button(self.root, text="Edit User", command=self.Test).grid(column=3, row=1, columnspan=1)
        self.root.mainloop()
    def New_Open_Window(self):
        self.root = Window("Login")
        self.root.Add_Field("Username",0,0,75,8,2)
        self.root.Add_Field("Password",0,1,75,8,2)
        self.root.Add_Button("Log In",6,0,self.Log_In,10,8,1)
        self.root.Add_Button("Edit User",6,1,self.Edit_Users,10,8,1)
        self.root.Create_Window()
