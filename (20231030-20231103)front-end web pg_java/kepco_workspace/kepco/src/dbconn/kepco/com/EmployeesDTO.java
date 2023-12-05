package dbconn.kepco.com;

import java.sql.Timestamp;

public class EmployeesDTO {
	private int empoyeeId;
	private String firstname;
	private String email;
	private Timestamp hireDate;
	public int getEmpoyeeId() {
		return empoyeeId;
	}
	public void setEmpoyeeId(int empoyeeId) {
		this.empoyeeId = empoyeeId;
	}
	public String getFirstname() {
		return firstname;
	}
	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public Timestamp getHireDate() {
		return hireDate;
	}
	public void setHireDate(Timestamp hireDate) {
		this.hireDate = hireDate;
	}
	@Override
	public String toString() {
		return "EmployeesDTO [empoyeeId=" + empoyeeId + ", firstname=" + firstname + ", email=" + email + ", hireDate="
				+ hireDate + "]";
	}
	
	
	
}

