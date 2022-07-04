class UserList:
    class User_Template:
        def __init__(self, Username, Priv_Level, PW_Hash, First_Name, Last_Name, Email=None, Phone=None):
            self.Username = Username if Username!=None else "Guest"
            self.PrivLevel = Priv_Level if Priv_Level!=None else "Guest"
            self.PW_Hash = PW_Hash if PW_Hash!=None else "Guest"
            self.Email = Email if Email!=None else "Nobody@nowhere.net"
            self.Phone = Phone if Phone!=None else "+16508675309"
            self.First_Name = First_Name
            self.Last_Name = Last_Name
    def __init__(self):
        self.TheList = {}
    def Add_User(self):
        pass
    def Edit_User(self):
        pass
    def Delete_User(self):
        pass
