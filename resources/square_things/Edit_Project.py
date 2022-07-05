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
        #Initialize window
    
        self.root = Tk()
        self.root.title("Edit Project")
        
        self.author_label = Label(self.root,text="Author:").grid(column=0,row=0,columnspan=1)
        self.author = Entry(self.root, width=30)
        self.author.grid(column=1, row=0, columnspan=1)
        
        self.date_label = Label(self.root,text="Date Submitted:").grid(column=2,row=0,columnspan=1)
        self.date_submitted = Entry(self.root)
        self.date_submitted.grid(column=3, row=0, columnspan=1)
        
        self.urgency_label = Label(self.root,text="Urgency:").grid(column=4,row=0,columnspan=1)
        self.urgency = Entry(self.root, width=30)
        self.urgency.grid(column=5, row=0, columnspan=1)
        
        self.title = Entry(self.root, width=75)
        self.title.grid(column=1, row=1, columnspan=3)
        self.title_label = Label(self.root,text="Title:").grid(column=0,row=1,columnspan=1)
        
        self.description_label = Label(self.root,text="Description:").grid(column=0,row=2,columnspan=1)
        self.description = Entry(self.root, width=75)
        self.description.grid(column=1, row=2, columnspan=3)
        
        self.due_date_label = Label(self.root,text="Due Date:").grid(column=4,row=1,columnspan=1)
        self.date_due = Entry(self.root, width=30)
        self.date_due.grid(column=5, row=1, columnspan=1)
        
        self.assignee_label = Label(self.root,text="Assignee:").grid(column=4,row=2,columnspan=1)
        self.assignee = Entry(self.root, width=30)
        self.assignee.grid(column=5, row=2, columnspan=1)
        
    
        
        
        
        Button(self.root, text="Add Attachments", command=None).grid(column=3, row=10, columnspan=2)
        Button(self.root, text="Save", command=self.Save_Project).grid(column=4, row=11, columnspan=2)
        Button(self.root, text="Cancel", command=self.Close_Window).grid(column=5, row=11, columnspan=2)
        # Button(self.root, text="Delete Attachment", command=None).grid(column=0, row=5, columnspan=2)
        self.root.mainloop()
    def Close_Window(self):
        self.root.destroy()
    def Save_Project(self):
        # Get info from fields and insert them into the Ticket class
        # Pass this info to the landing page
        # Close window
