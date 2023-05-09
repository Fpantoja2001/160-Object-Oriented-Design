public class Person {
	public String name;
	public String address;
	public String phone;
	Person(String name, String address, String phone) {
		this.name = name;
		this.address =  address;
		this.phone = phone;
	}
	void setName(String n) {
		name = n;
	}
	public String getName() {
		return name;
	}
	public String getPhone() {
		return phone;
	}
	public String toString() {
		return "Name: " + name + "\nAddress: " + address + "\nPhone: " + phone;
	}
}
