package kepco.human.com;

import java.util.Random;

public class Lotto {
	private Random rd = null;
	private int[] lotto = new int[6];

	
	public void makelotto() {
		rd=new Random();
		lotto[0]=rd.nextInt(45)+1;
		for(int i=1; i<6;i++) {
			int temp=rd.nextInt(45)+1;
			//내가 작성
//			for(int j=0; j<i;j++) {
//				if(temp != lotto[j]) {
//					lotto[i]=temp;
//				}else {
//					i--;
//				}
//			}
			//결과는 나오지만 필요없는 for문이 돌고 있음
//			lotto[i]=temp;
//			for(int j=0; j<i;j++) {
//				if(temp == lotto[j]) {
//					i--;
//				}
//			}
			//최선
			lotto[i]=temp;
			for(int j=0; j<i;j++) {
				if(temp == lotto[j]) {
					i--;
					break;
				}
			}
		}
		for(int value :lotto) {
		System.out.println("[ "+value+" ]");
		}
		System.out.println();
	}

	public static void main(String[] args) {
		new Lotto().makelotto();
	}
}


//조합의 경우의 수(45C6)   (6*5*4*3*2*1)/(45*44*43*42*41*40)
//자바의 random이라는 클래스를 이용하여 난수를 발생하자.