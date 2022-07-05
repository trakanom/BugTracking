class Ticket:
    def __init__(self,author, date_submitted, urgency, title, description, date_due=None, assignee=None):
        self.author=author
        self.date_submitted=date_submitted
        self.urgency=urgency
        self.title=title
        self.description=description
        self.date_due=date_due
        self.assignee=assignee
        self.updates = {}
        self.attachments = {}

