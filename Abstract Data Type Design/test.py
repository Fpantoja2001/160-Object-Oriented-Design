import unittest
from Person import Person
from Persons import Persons

class testAssignment(unittest.TestCase):
    def test_get_name_sofia(self):
        person1 = Person()
        person1.setName('Jaime')
        self.assertTrue('Jaime',person1.getName())

    def test_get_salary_35(self):
        person1 = Person()
        person1.setSalary(35)
        self.assertTrue(35,person1.getSalary())

    def test_display_complete_directory(self):
        persons = Persons()
        persons.enterNewPerson(Person('Jaime','Amherst',35))
        self.assertTrue(persons.listOfPersons[0],persons.displayCompleteDirectory())

    def test_search_for_person(self):
        persons = Persons()
        persons.enterNewPerson(Person('Jaime','Amherst',35))
        self.assertTrue(persons.listOfPersons[0],persons.searchForPerson('jaime'))

if __name__ == '__main__':
    unittest.main()