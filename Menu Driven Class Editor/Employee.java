public class Employee extends Person{
	private String department;
	
	Employee(String name, String address, String phone, String department) {
		super(name, address, phone);
		this.department = department;
	}
	String getDepartment() {
		return this.department;
	}
	void setDepartment(String department) {
		this.department = department;
	}
	public String toString() {
		String d = "Year: " + department;
		return super.toString() + "\n" + d;
	}
}
