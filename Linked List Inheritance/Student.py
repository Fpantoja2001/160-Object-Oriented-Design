from Person import Person

class Student(Person):
    def __init__(self,newName='none',address='none',phone='999-999-9999',year=9999):
        self.name = newName
        self.address = address
        self.phone = phone
        self.year = year
    
    def setGraduationYear(self,graduationYear):
        self.year = graduationYear
    
    def getGraduationYear(self):
        return self.year
    
    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}\nYear: {self.year}'
