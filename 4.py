from datetime import datetime

class Person:
    def __init__(self,first_Name,last_Name,doB):
        self.last_Name = str(last_Name)
        self.first_Name = str(first_Name)
        self.doB = datetime.strptime(doB, "%d-%m-%Y")
    
    def ages(self):
        return int((datetime.now() - self.doB).days / 365.25)
