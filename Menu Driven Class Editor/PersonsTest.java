import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class PersonsTest{
    
    @Test
    public void addTest1() {
        Persons p = new Persons();
        Person test1 = new Person("Arien", "141 Orchard Hill", "774-578-0137");
        p.add(test1);
        assertEquals(true, p.getSize() == 1);
    }

    @Test
    public void addTest2() {
        Persons p = new Persons();
        Person test1 = new Person("Arien", "141 Orchard Hill", "774-578-0137");
        Person test2 = new Person("Errine", "141 Orchard Hill", "774-578-0137");
        p.add(test1);
        p.add(test2);
        assertEquals(true, p.getSize() == 2);
    }

    @Test
    public void deleteTest1() {
        Persons p = new Persons();
        Person test1 = new Person("Arien", "141 Orchard Hill", "774-578-0137");
        p.add(test1);
        p.delete(0);
        assertEquals(true, p.getSize() == 0);
    }

    @Test
    public void deleteTest2() {
        Persons p = new Persons();
        Person test1 = new Person("Arien", "141 Orchard Hill", "774-578-0137");
        Person test2 = new Person("Errine", "141 Orchard Hill", "774-578-0137");
        p.add(test1);
        p.add(test2);
        p.delete(0);
        assertEquals(true, p.getSize() == 1);
    }
}