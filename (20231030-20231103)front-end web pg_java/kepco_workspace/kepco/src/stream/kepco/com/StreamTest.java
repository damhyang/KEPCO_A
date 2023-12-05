package stream.kepco.com;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;

public class StreamTest {
	int temp;
	FileInputStream fi;
	FileOutputStream fo;
	
	public void test() {
		try {
			fi=new FileInputStream("c:/kepco_workspace/a.txt");
			fo = new FileOutputStream("c:/kepco_workspace/b.txt");
			while((temp = fi.read())!=-1) {
				System.out.print((char)temp);
				fo.write((char)temp);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			try{
			fi.close();
			fo.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
		
	public void test1() {
		FileReader fr=null;
		FileWriter fw=null;
		
		try {
			fr = new FileReader("c:/kepco_workspace/a.txt");
			fw = new FileWriter("c:/kepco_workspace/c.txt");
			while((temp = fr.read())!=-1) {
//				System.out.print((char)temp);
				fw.write((char)temp);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			try{
			fr.close();
			fw.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	
	public static void main(String[] args) {
		new StreamTest().test();
		new StreamTest().test1();

	}

}
