# from ...resources.configurator import MasterList
from tkinter import *


class Login:
    def __init__(self,Userlist):
        self.Userlist = Userlist
        pass
    def Test(self):
        print("Pass")
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
        except:
            from .Error import ErrorPage
            print('Error("Incorrect Information")')
            self.Error = ErrorPage("Incorrect Information")
        pass

    def OpenWindow(self):
        #Initialize window with fields for username & password, and buttons for logging in and editing users
        self.root = Tk()
        self.username = Entry(self.root, width=30)
        self.password = Entry(self.root,width=30)
        self.username.grid(column=0,row=0,columnspan=2)
        self.password.grid(column=0,row=1,columnspan=2)
        Button(self.root, text="Log In", command=self.Log_In).grid(column=3, row=0, columnspan=1)
        Button(self.root, text="Edit User", command=self.Test).grid(column=3, row=1, columnspan=1)
        self.root.mainloop()