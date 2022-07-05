from tkinter import *
from ..classes.Tickets import Ticket
import time
class Project_Window:
    def __init__(self, Userlist, username, Project=None):
        self.Userlist = Userlist
        self.username = username
        self.Project = Ticket(author=self.username, date_submitted=time.localtime, urgency="Low", title="Test", description="Blank Description", date_due=None, assignee=None) if Project==None else Project
        print(self.Project.author)
    def Populate_Window(self):
        #When editing a project, prefill all fields with project info.
        #When adding a project, prefill all fields with basic info.
        pass
    def Open_Window(self):
        pass
        #Initialize window
    
    def Close_Window(self):
        self.root.destroy()
    def Save_Project(self):
        # Get info from fields and insert them into the Ticket class
        # Pass this info to the landing page
        # Close window
