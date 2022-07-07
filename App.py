#Loads important packages
#Opens login window
#After authentication, loads data into ram
from resources.square_things.Login import Login
from resources.classes.Userlists import UserList

# To be placed elsewhere after testing
# Initialize the Userlist
MasterList = UserList()
MasterList.Add_User(Username="Trakanom", Priv_Level="Owner", PW_Hash="Hunter2", First_Name="Mika", Last_Name="Wisener-Brandt")
#Eventually want this to be     a default import upon program load

#Testing Login functionality
newLogin = Login(MasterList)


newLogin.New_Open_Window()