package dbconn.kepco.com;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBconnSingleTon {
//singleTon 객체는 메모리에 1개만 인스턴스화 하여 사용하는 방법
//그래서 아래와 같이 만들어야함.
//1. 외부에서 new해서 못만들도록 해야함.->생성자를 private선언해버림.
//같은 클래스 내에서 접근자(dst) 생성
	
	private static DBconnSingleTon dst=new DBconnSingleTon();
	Connection conn;
	
	private DBconnSingleTon() {
		try {
			conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/hr","hr","1234");
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	
	public static DBconnSingleTon getInstance() {
		if(dst==null) {
			dst=new DBconnSingleTon();
		}
		return dst;
	}
	
	public Connection getConnection() {
		return conn;
	}
}
