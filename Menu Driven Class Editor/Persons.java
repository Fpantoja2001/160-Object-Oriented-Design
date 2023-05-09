import java.util.ArrayList;

public class Persons{
	ArrayList<Person> listOfPersons = new ArrayList<Person>();
	
	public Persons search(String s){
		Persons newList = new Persons();
		for (Person p: listOfPersons){
			if (p.getName().equals(s)){
				newList.add(p);
			}
		}
		return newList;
	}

	public void add(Person p){
		listOfPersons.add(p);
	}

	public int getSize(){
		return listOfPersons.size();
	}

	public void delete(int i){
		listOfPersons.remove(i);
	}

	public ArrayList<Person> getInternalList(){
		return listOfPersons;
	}

	public void displayComepleteDirectory(){
		for(Person p: listOfPersons){
			System.out.println("\n------------\n" + p);
		}
	}
}