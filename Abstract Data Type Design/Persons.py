from Person import Person

class Persons:
    def __init__(self,):
        self.listOfPersons = []

    def displayCompleteDirectory(self):
        strOfEntireDirectory = ''
        for i in self.listOfPersons:
            strOfEntireDirectory += str(i) + '\n'
        return strOfEntireDirectory
    
    def searchForPerson(self,stringOfPersonBeingSearched):
        strOfRecords = ''
        for i in self.listOfPersons:
            if stringOfPersonBeingSearched.lower() in str(i).lower():
                strOfRecords += str(i)
        return strOfRecords
    
    def enterNewPerson(self,objectOfNewPerson):
        self.listOfPersons.append(objectOfNewPerson)
    
    def modifyPersonInformation(self,stringOfPersonBeingModified):
        strOfRecords = ''
        tempIndex = 0
        for i in self.listOfPersons:
            if stringOfPersonBeingModified in str(i):
                strOfRecords += str(i)
                tempIndex = self.listOfPersons.index(i)
        decision = input('Would you like to modify this record at index ' + str(tempIndex) + '?\n' + strOfRecords + '\n\nEnter number of Selection:\n1) Yes\n2) No\n')
        
        if decision == '1':
            modificationSelector = input('What would you like to Modify? Enter Number of Selection to Choose. \n1) Name\n2) Salary\n3) Adress\n')
            newValue = input('Perfect! Now enter the new value: ')

            if modificationSelector == '1':
                self.listOfPersons[tempIndex].setName(newValue)
            if modificationSelector == '2':
                self.listOfPersons[tempIndex].setSalary(newValue)
            if modificationSelector == '3':
                self.listOfPersons[tempIndex].setAdress(newValue)
        else:
            return 'You selected No, so the program will quit.'
    
    def deleteARecord(self,stringOfRecordBeingDeleted):
        strOfRecords = ''
        tempIndex = 0
        for i in self.listOfPersons:
            if stringOfRecordBeingDeleted in str(i):
                strOfRecords += str(i)
                tempIndex = self.listOfPersons.index(i)
        decision = input('Would you like to delete this Record at index ' + str(tempIndex) + '?\n' + strOfRecords + '\n\nEnter number of Selection:\n1) Yes\n2) No\n')
        
        if decision == '1':
            self.listOfPersons.pop(tempIndex)
            return 'Sucessfully Deleted.'
        else:
            return 'You selected No, so the program will quit.'
        

if __name__ == "__main__":

    pass