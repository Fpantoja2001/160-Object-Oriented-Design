class Person():

    def __init__(self, newName="none", address="none", phone="999-999-9999", department="none", salary=15):
        self.name = newName
        self.address = address
        self.phone = phone
        self.department = department
        self.hourlySalary = salary

    def setName(self, name):
        self.name = name

    def getName(self):
        return(self.name)

    def setSalary(self, newSalary):
        self.hourlySalary = newSalary

    def getSalary(self):
        return(self.hourlySalary)

    def getAddress(self):
        return(self.address)
    
    def setAdress(self,newAdress):
        self.address = newAdress

    def __str__(self):
        return 'Name: ' + str(self.getName()) + '\nSalary: ' + str(self.getSalary()) + '\nAddress: ' + str(self.getAddress())
        

if __name__ == '__main__':
   print("Hello World")