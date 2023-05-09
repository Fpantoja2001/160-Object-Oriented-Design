from Person import Person

class Employee(Person):
    def __init__(self,newName='none',address='none',phone='999-999-9999',department='not assigned'):
        self.name = newName
        self.address = address
        self.phone = phone
        self.department = department
    
    def setDepartment(self,newDepartment):
        self.department = newDepartment

    def getDepartment(self):
        return self.department
    
    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}\nDepartment: {self.department}'
