package stream.kepco.com;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;

public class StreamTest2 {
	int temp;
	FileInputStream fi;
	FileOutputStream fo;
	
		
	public void test3() {
		//1.8버전까지는 아래와 같이 사용해야함.
		try (
			FileReader fr = new FileReader("c:/kepco_workspace/a.txt");
			FileWriter fw = new FileWriter("c:/kepco_workspace/d.txt");
		){
			while((temp = fr.read())!=-1) {
				fw.write((char)temp);
		}
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void test4() throws Exception{
		//1.9이후는 아래와 같이 사용 가능
			FileReader fr = new FileReader("c:/kepco_workspace/a.txt");
			FileWriter fw = new FileWriter("c:/kepco_workspace/e.txt");
		try(fr;fw){
			while((temp = fr.read())!=-1) {
//				System.out.print((char)temp);
				fw.write((char)temp);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	
	
	public static void main(String[] args) throws Exception{
		new StreamTest2().test3();
		new StreamTest2().test4();
	}
}
