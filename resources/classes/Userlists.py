import sys
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
            self.Projects = {}
    def __init__(self):
        self.TheList = {}
    def Add_User(self, Username, Priv_Level, PW_Hash, First_Name, Last_Name, Email=None, Phone=None):
        self.TheList[Username]=self.User_Template(Username, Priv_Level, PW_Hash, First_Name, Last_Name, Email, Phone)
    def Edit_User(self):
        pass
    def Delete_User(self):
        pass
    def Add_Project(self,user,Project):
        self.TheList[user].Projects[Project["Title"]]=Project
        #Save project as dict to data\users\{User}\{Project_Title}.py
        directory = 'data\\users\\'+str(user)+'\\'+str(Project["Title"].replace(" ","_"))+'.py' 
            
            
        r = open(directory, "x")
        #Form an importable, formatted dict saved as a file for future references.
        r.write("Project = {")
        for n,key in enumerate(Project.keys()):
            string = f"\t\"{key}\":\"{Project[key]}\""
            r.write((",\n" if n>0 else "\n")+string)
        r.write("}")