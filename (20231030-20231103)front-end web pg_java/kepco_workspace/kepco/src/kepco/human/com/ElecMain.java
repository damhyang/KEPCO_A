package kepco.human.com;

public class ElecMain {
	public void test() {
		
	}
//	public static void main(String[] args) {
//		test();test메소드에 static을 선언하지 않으면 인스턴스화되지 않아 에러가남.
//	}
	public static void main(String[] args) {
		GenericTest gt = new GenericTest();
		gt.test();
		gt.result();
	}
}
