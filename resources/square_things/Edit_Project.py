from tkinter import *
from ..classes.Tickets import Ticket
from ..classes.Windows import Window
from ..config import config
from datetime import datetime
class Project_Window:
    def __init__(self, Userlist, username, Project=None):
        self.Userlist = Userlist
        self.username = username
        now=datetime.now()
        self.now = now.strftime("%d/%m/%Y %H:%M:%S")
        self.Project = Ticket(author=self.username, date_submitted=self.now, urgency="Low", title="Test", description="Blank Description", date_due=None, assignee=None) if Project==None else Project
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
    def New_Open_Window(self):
        self.root=Window("Edit Project")
        self.root.Add_Dropdown("Author",self.Userlist.TheList.keys(),column=0,row=0,default_text="none")
        self.root.Add_Dropdown("Urgency",config["ticketPriorities"],column=0,row=1,default_text="none")
        self.root.Add_Dropdown("Difficulty",config["ticketDifficulty"],column=0,row=2,default_text="none")
        self.root.Add_Dropdown("Assignee",self.Userlist.TheList.keys(),column=2,row=1,default_text="none")

        self.root.Add_Field("Date Submitted",column=2,row=0,default_value=self.now)
        self.root.Add_Field("Date Due",column=2,row=2)
 
        self.root.Add_Field("Title",column=0,row=3,width=75,columnspan=4)
        self.root.Add_Field("Description",column=0,row=4,width=75,height=40,columnspan=4)
        self.root.Add_Button("Add Attachments",column=0,row=6,command=None)
        self.root.Add_Button("Save",column=3,row=6,command=self.New_Save_Project)
        self.root.Add_Button("Cancel",column=5,row=6,command=self.Close_Window)
        
        pass
    def Close_Window(self):
        self.root.Close_Window()
    def Save_Project(self):
        # Get info from fields and insert them into the Ticket class
        # Pass this info to the landing page
        # Close window
        NewPage = Ticket(author=self.author.get(), 
                            date_submitted=self.now, 
                            urgency=self.urgency.get(),
                            title=self.title.get(), 
                            description=self.description.get(), 
                            date_due=self.date_due.get(), 
                            assignee=self.assignee.get())
    def New_Save_Project(self):
        Saved = self.root.Get_Fields(*self.root.fields.keys())
        print(Saved)
        self.Userlist.Add_Project(self.username,Saved)