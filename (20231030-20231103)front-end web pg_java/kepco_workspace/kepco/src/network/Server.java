package network;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
	private ServerSocket ss;
	private Socket innerSocket;
	
	public void serverStart() throws Exception {
		ss = new ServerSocket(23333);
		System.out.println("서버 소켓이 생성되었습니다");
		while(true) {
			System.out.println("클라이언트의 접속을 기다립니다");
			innerSocket= ss.accept();
			System.out.println("클리이언트가 접속 했습니다.");
			getMessage(innerSocket);
		}		
	}
	
	public void getMessage(Socket innerSocket) throws Exception{
		InputStream is=innerSocket.getInputStream();		
		InputStreamReader isr = new InputStreamReader(is);		
		BufferedReader br = new BufferedReader(isr);
		
//		OutputStream os=innerSocket.getOutputStream();
//		OutputStreamWriter osw = new OutputStreamWriter(os);		
//		BufferedWriter bw = new BufferedWriter(osw);
//		bw.write("어서 오이소");
//		bw.flush();
		
		PrintWriter pw = new PrintWriter(innerSocket.getOutputStream(),true);
		pw.println("어서오세요");
		
		String chat = br.readLine();
		System.out.println("클라이언가 보낸 문자열: " + chat);
		
		br.close();
		pw.close();
	}

	public static void main(String[] args) throws Exception {
		Server sv= new Server();
		sv.serverStart();
	}

}
