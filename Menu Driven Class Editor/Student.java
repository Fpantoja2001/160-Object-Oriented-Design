public class Student extends Person{
	private int year;
	Student(String name, String address, String phone, int year) {
		super(name, address, phone);
		this.year = year;
	}

	int getGraduationYear() {
		return this.year;
	}
	public void setGraduationYear(int year) {
		this.year = year;
	}
	public String toString() {
		String y = "Year: " + year;
		return super.toString() + "\n" + y;

	}
}
