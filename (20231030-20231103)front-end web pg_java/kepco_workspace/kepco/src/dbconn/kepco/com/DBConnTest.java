package dbconn.kepco.com;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBConnTest {
	private Connection conn;
	private PreparedStatement pstm;  
	private ResultSet rs;

//	public void connectDB() throws Exception{
//	conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/hr","hr","1234");
//	}
	
	
	
	public void select() throws Exception{
		conn=DBconnSingleTon.getInstance().getConnection();
		String query = "SELECT EMPLOYEE_ID, FIRST_NAME, EMAIL, HIRE_DATE FROM EMPLOYEES";
		pstm = conn.prepareStatement(query);		
//			1.실행하는 쿼리문이 select문일 경우 excuteQuery()
//			2. insert, update, delete일 경우는 excuteUpdatd()
		rs = pstm.executeQuery();

		while(rs.next()) {
			int employeeId=rs.getInt("employee_id");
			String firstName= rs.getString("first_name");
			String email = rs.getString("email");
			String hireDate=rs.getString("hire_date");
		 	System.out.println(employeeId+"  "+firstName+"  "+email+"  "+hireDate);
			System.out.println();
		}
	}
	
	public void insert() throws Exception{
//		String query =  "INSERT INTO EMPLOYEES VALUES('','A','AA','AAA','AAAA',NOW(),'AD_VP',6000,NULL,110,30)"
		StringBuilder sb = new StringBuilder();
		sb.append("INSERT INTO EMPLOYEES VALUES");
		sb.append("(300,'A','AA','AAA','AAAA',NOW(),'AD_VP',6000,NULL,110,30)");
		pstm=conn.prepareStatement(sb.toString());
		pstm.executeUpdate();
		conn.setAutoCommit(false);
	}
	
	public static void main(String[] args) throws Exception {
		DBConnTest dt = new DBConnTest();
//		dt.connectDB();
		dt.select();
		dt.insert();

	}

}

//싱글톤 메소드는 new가 안됨.
