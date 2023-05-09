class Person:
    def __init__(self,newName='none',address='none',phone='999-999-9999'):
        self.name = newName
        self.address = address
        self.phone = phone
    
    def setName(self,stringOfName):
        self.name = stringOfName
    
    def getName(self):
        return self.name
    
    def getPhone(self):
        return self.phone
    
    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}'
    
    