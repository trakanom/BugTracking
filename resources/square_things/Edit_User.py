from tkinter import *
# from tokenize import String
from ..classes.Windows import Window
from ..config import config
class Edit_Users:
    def __init__(self,userlist,user):
        self.UserList = userlist
        self.User = user
        pass
    def Add_User(self):
        pass
    def Edit_User(self):
        pass
    def Delete_User(self):
        pass
    def Open_Window(self):
        self.square = Window("Edit User")
        self.square.Add_Dropdown("Users",column=0,row=0,default_text="Pick a user",contents=self.UserList.TheList)
        self.square.Add_Button("Add User",0,1,lambda: self.Add_User)
        self.square.Add_Button("Edit User",0,2,lambda: self.Edit_User)
        self.square.Add_Button("Delete User",0,3,lambda: self.Delete_User)
        self.square.Add_Button("Cancel",0,5,self.Close_Window)
        self.square.Create_Window()
    def Close_Window(self):
        from .Login import Login
        nextWindow = Login(self.UserList)
        self.square.Close_Window()
        nextWindow.New_Open_Window()