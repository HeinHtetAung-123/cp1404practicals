import datetime
FULL_COMPLETION =100
class Project:
    def __init__(self,name="",start_date="",priority=int,cost=float,completion=int):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date,"%d/%m/%Y").date()
        self.priority = priority
        self.cost =cost
        self.completion = completion

    def __str__(self):
        """Returning a string of the representation of the project"""
        return f"{self.name}, Starts: {self.start_date}, Priority: {self.priority}, Cost: ${self.cost:.2f}, Completion: {self.completion}%"

    def is_complete(self):
        """Checking if the project is completed."""
        return int(self.completion) == FULL_COMPLETION

    def __lt__(self, other):
        """Comparing projects' priority with this less than method"""
        return self.priority<= other.priority

    def compare_date(self,input_date):
        """Checking if the start date of the project is after the input date."""
        input_date = datetime.datetime.strptime(input_date,"%d/%m/%Y").date()
        return self.start_date>=input_date

    def update_percentage(self,value):
        """Updating  the project's percentage of completion"""
        self.completion = value

    def update_priority(self,value):
        """Updating the project's priority."""
        self.priority = value