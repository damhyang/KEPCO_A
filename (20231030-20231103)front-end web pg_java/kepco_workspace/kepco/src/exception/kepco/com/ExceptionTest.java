package exception.kepco.com;

public class ExceptionTest {
//반드시 예외처리를 해야하는 경우...하지 않으면 문법적으로 에러임
	//외부와의 접촉
//	1.DB접속할 경우.
//	2.네트워크 접속할 경우
//	3.I/O..스트림
//	4.쓰레드 사용
	
	public void test() {
		try {
			int result=10/0;
		}catch(Exception e) {
			System.out.println("분모로 0이 오면 안되요");
			e.printStackTrace();
			e.getMessage();
		}finally {
			System.out.println("예외가 발행하나 하지 않으나 수행됩니다.");
		}
	}
	
	public void test1() throws Exception{   //예외가 넘어감.
		int result=10/0;
	}
	
	public void test2() {
		try {
			int result=10/0;
		}catch(Exception e) {
			new KepcoException(e);
		}
	}
	
	public static void main(String[] args) {
		try {
			new ExceptionTest().test2();
		}catch(Exception e) {
			System.out.println("메인메소드에서 예외처리");
			e.printStackTrace();
		}
		

	}

}
