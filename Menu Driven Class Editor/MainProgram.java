import java.util.Scanner;

public class MainProgram {

	public static void menuDisplay() {
		System.out.print("Enter option from list below:\n"
			+ "   1) Display Comeplete Directory\n"
			+ "   2) Enter new Person\n"
			+ "   3) Search for Person\n"
			+ "   4) Modify Person Information\n"
			+ "   5) Delete a record\n"
			+ "   Q) Quit\n"
			+ "Enter your option: ");
	}

	public static void enterNewPerson(Persons p, Scanner scanner) {
		System.out.print("Enter New Person Name: ");
		String newPersonName = scanner.next();
		System.out.print("Enter New Person Address: ");
		String newPersonAddress = scanner.next();
		System.out.print("Enter New Person Phone: ");
		String newPersonPhone = scanner.next();
		System.out.print("Is this new person an:"
				+ "\n  1) Employee"
				+ "\n  2) Student"
				+ "\nEnter your option: ");
		String personObjDecider = scanner.next();

		if (personObjDecider.equals("1")) {
			System.out.print("Enter New Employee Department: ");
			String newPersonDepartment = scanner.next();
			Employee newE = new Employee(newPersonName,newPersonAddress,newPersonPhone,newPersonDepartment);
			p.add(newE);
		} else if (personObjDecider.equals("2")) {
			System.out.print("Enter New Student Year: ");
			int newPersonYear = scanner.nextInt();
			Student newS = new Student(newPersonName,newPersonAddress,newPersonPhone,newPersonYear);
			p.add(newS);
		}
	}

	public static void mainDelete(Persons p, Scanner k){
		System.out.print("Which entry do you wish to delete: ");
		int entryToDelete = k.nextInt();

		if(entryToDelete < 0 || entryToDelete > p.getSize()){
			System.out.print("\nError: Index is not within range of entries. Nothing was deleted.\n\n");
			p.displayComepleteDirectory();
		} else {
			System.out.println(p.listOfPersons.get(entryToDelete));
			System.out.print("Enter Y if this is what you wanted to delete: ");
			String option = k.next();
			
			if (option.toLowerCase().equals("y")){
				p.delete(entryToDelete);
				System.out.print("New Directory");
				p.displayComepleteDirectory();
			}
		}
	}

	public static void mainModify(Persons p, Scanner k){	
		System.out.print("Enter the name of the person you want to modify: ");
		String name = k.next();
		p.search(name);

		for(Person d: p.listOfPersons){
			if(d.getName().equals(name)){
				System.out.println(d.toString());
				System.out.print("Do you wish to modify this Object?: ");
				String option = k.next();

				if(option.toLowerCase().equals("y")){
					System.out.println("What is the items new name?: ");
					String newName = k.next();
					d.setName(newName);
				}
			} else {
				System.out.println("\nError: There is no one by that name or it is an invalid entry. Try again.\n");
			}
		}
	}

	public static void mainSearch(Persons p, Scanner k){
		System.out.print("Enter the name of the person you're searching for: ");
		String peopleToReturn = "";
		String option = k .next();

		for(Person z: p.listOfPersons){
			if(z.getName().equals(option)){
				peopleToReturn += "--------------\n" + z.toString() + "\n";
			}
		}
		if (peopleToReturn.equals("")){
			System.out.print("\nSorry, no one matched that name. Try again.\n\n");
		} else {
			System.out.print(peopleToReturn);
		}
	}

	public static void main(String args[]){
		Persons p = new Persons();
		Scanner userInput = new Scanner(System.in);
		menuDisplay();
		String option = userInput.nextLine();

		while (true){
			if (option.equals("1")) {
				p.displayComepleteDirectory();
				menuDisplay();
				option = userInput.next();
				
			} else if (option.equals("2")) {
				enterNewPerson(p,userInput);
				menuDisplay();
				option = userInput.next();
				
			} else if (option.equals("3")) {
				mainSearch(p, userInput);
				menuDisplay();
				option = userInput.next();
				
			} else if (option.equals("4")) {
				mainModify(p,userInput);
				menuDisplay();
				option = userInput.next();
				
			} else if (option.equals("5")) {
				mainDelete(p, userInput);
				menuDisplay();
				option = userInput.next();
				
			} else if (option.toLowerCase().equals("q")) {
				break;
			} else {
				System.out.print("\nError: Invalid entry. Try Again.\n\n");
				menuDisplay();
				option = userInput.next();
			}
		}
		userInput.close();
	}
}