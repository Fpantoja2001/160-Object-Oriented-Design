from Node import Node
from Person import Person
from Employee import Employee
from Student import Student
import unittest


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self):
        return(self.size)

    def add(self, e):
        n = Node()
        n.setData(e)
        if self.size == 0:
            self.head = n
            self.tail = n
        else:
            currentlyTheLastElement = self.tail
            n.setPrevious(currentlyTheLastElement)
            currentlyTheLastElement.setNext(n)
            self.tail = n
        self.size = self.size + 1
                
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        stringToReturn = ""
        for e in self:
            stringToReturn = stringToReturn + str(e) + "\n"
        return(stringToReturn)
    

    def __getitem__(self, i):
        if not(i > self.size):
            curr = self.head
            elementsPassed = 0
            while curr is not None:
                if elementsPassed == i:
                    return curr.getData()
                else:
                    curr = curr.next  
                    elementsPassed += 1

    def directory(self):
        curr = self.head
        while curr:
            print(str(curr))
            curr = curr.next

    def insert(self,i,objBeingInserted):
        newObj = Node()
        newObj.setData(objBeingInserted)

        #Case where you insert at the head
        if i == 0:
            newObj.setNext(self.head)
            self.head.setPrevious(newObj)
            self.head = newObj
        #Case where you insert at the tail
        elif i == self.size:
            self.add(objBeingInserted)
        #Case where you insert in the middle
        else:
            curr = self.head
            while curr is not None:
                if curr.getData() == self[i]:
                    backObj = curr.getPrevious()
                    backObj.setNext(newObj)
                    curr.setPrevious(newObj)
                    newObj.setPrevious(backObj)
                    newObj.setNext(curr)
                curr = curr.getNext()

    def delete(self,i):
            curr = self.head
            prev = curr.getPrevious()
            while curr is not None:
                if curr.getData() == self[i]:
                    if prev == None:
                        self.head = curr.getNext()
                        break
                    else:
                        prev.next = curr.next
                        curr.next = None
                        break
                else:
                    prev = curr
                    curr = curr.next

    def search(self,strBeingSearchedFor):
        curr =  self.head
        newLinkedList = LinkedList()
        while curr:
            if strBeingSearchedFor == (curr.getData()).getName():
                newLinkedList.add(curr.getData())
            curr = curr.getNext()
        return newLinkedList
    
class test(unittest.TestCase):
    def test_insert_head(self):
        #Creates new object
        samplePerson5 = (Person('5','Webster','123-456-7890'))
        sampleStudent5 = (Student('5','Webster','123-456-7890',2026))
        sampleEmployee5 = (Employee('5','Webster','123-456-7890','Dance'))
        #Inserts new object at index
        People1.insert(0,samplePerson5)
        Students1.insert(0,sampleStudent5)
        Employees1.insert(0,sampleEmployee5)
        #Checks if new objcet exists at index
        self.assertEqual(People1[0],samplePerson5)
        self.assertEqual(Students1[0],sampleStudent5)
        self.assertEqual(Employees1[0],sampleEmployee5)

    def test_insert_middle(self):
        #Creates new object
        samplePerson5 = (Person('5','Webster','123-456-7890'))
        sampleStudent5 = (Student('5','Webster','123-456-7890',2026))
        sampleEmployee5 = (Employee('5','Webster','123-456-7890','Dance'))
        #Inserts new object at index
        People1.insert(1,samplePerson5)
        Students1.insert(1,sampleStudent5)
        Employees1.insert(1,sampleEmployee5)
        #Checks if new object exists at index
        self.assertEqual(People1[1],samplePerson5)
        self.assertEqual(Students1[1],sampleStudent5)
        self.assertEqual(Employees1[1],sampleEmployee5)
        
    def test_insert_tail(self):
        #Creates new object
        samplePerson5 = (Person('5','Webster','123-456-7890'))
        sampleStudent5 = (Student('5','Webster','123-456-7890',2026))
        sampleEmployee5 = (Employee('5','Webster','123-456-7890','Dance'))
        #Inserts new object at index
        People.insert(4,samplePerson5)
        Students.insert(4,sampleStudent5)
        Employees.insert(4,sampleEmployee5)
        #Checks if new object exists at index 
        self.assertEqual(People[4],samplePerson5)
        self.assertEqual(Students[4],sampleStudent5)
        self.assertEqual(Employees[4],sampleEmployee5)

    
    def test_delete_first_element(self):
        #Stores object from index
        personBeingDeleted = People1[0]
        studentBeingDeleted = Students1[0]
        employeeBeingDeleted = Employees1[0]
        #Deletes object from index
        People1.delete(0)
        Students1.delete(0)
        Employees1.delete(0)
        #Checks if object is still at the index
        self.assertNotEqual(People1[0],personBeingDeleted)
        self.assertNotEqual(Students1[0],studentBeingDeleted)
        self.assertNotEqual(Employees1[0],employeeBeingDeleted)

    def test_delete_middle_element(self):
        #Stores object from index
        personBeingDeleted = People1[1]
        studentBeingDeleted = Students1[1]
        employeeBeingDeleted = Employees1[1]
        #Deletes object from index
        People1.delete(1)
        Students1.delete(1)
        Employees1.delete(1)
        #Checks if object is still at the index
        self.assertNotEqual(People1[1],personBeingDeleted)
        self.assertNotEqual(Students1[1],studentBeingDeleted)
        self.assertNotEqual(Employees1[1],employeeBeingDeleted)

    def test_delete_last_element(self):
        #Stores object from index
        personBeingDeleted = People1[2]
        studentBeingDeleted = Students1[2]
        employeeBeingDeleted = Employees1[2]
        #Deletes object from index
        People1.delete(2)
        Students1.delete(2)
        Employees1.delete(2)
        #Checks if object is still at the index
        self.assertNotEqual(People1[2],personBeingDeleted)
        self.assertNotEqual(Students1[2],studentBeingDeleted)
        self.assertNotEqual(Employees1[2],employeeBeingDeleted)

        
if __name__== "__main__":

    #Tests
    
    People = LinkedList()
    Students = LinkedList()
    Employees = LinkedList()

    People1 = LinkedList()
    Students1 = LinkedList()
    Employees1 = LinkedList()

    samplePerson1 = (Person('1','Webster','123-456-7890'))
    samplePerson2 = (Person('2','Webster','123-456-7890'))
    samplePerson3 = (Person('3','Webster','123-456-7890'))
    samplePerson4 = (Person('4','Webster','123-456-7890'))

    sampleStudent1 = (Student('1','Webster','123-456-7890',2026))
    sampleStudent2 = (Student('2','Webster','123-456-7890',2026))
    sampleStudent3 = (Student('3','Webster','123-456-7890',2026))
    sampleStudent4 = (Student('4','Webster','123-456-7890',2026))

    sampleEmployee1 = (Employee('1','Webster','123-456-7890','Dance'))
    sampleEmployee2 = (Employee('2','Webster','123-456-7890','Dance'))
    sampleEmployee3 = (Employee('3','Webster','123-456-7890','Dance'))
    sampleEmployee4 = (Employee('4','Webster','123-456-7890','Dance'))

    People.add(samplePerson1)
    People.add(samplePerson2)
    People.add(samplePerson3)
    People.add(samplePerson4)

    People1.add(samplePerson1)
    People1.add(samplePerson2)
    People1.add(samplePerson3)
    People1.add(samplePerson4)

    Students.add(sampleStudent1)
    Students.add(sampleStudent2)
    Students.add(sampleStudent3)
    Students.add(sampleStudent4)

    Students1.add(sampleStudent1)
    Students1.add(sampleStudent2)
    Students1.add(sampleStudent3)
    Students1.add(sampleStudent4)

    Employees.add(sampleEmployee1)
    Employees.add(sampleEmployee2)
    Employees.add(sampleEmployee3)
    Employees.add(sampleEmployee4)

    Employees1.add(sampleEmployee1)
    Employees1.add(sampleEmployee2)
    Employees1.add(sampleEmployee3)
    Employees1.add(sampleEmployee4)

    unittest.main()

    


    
    