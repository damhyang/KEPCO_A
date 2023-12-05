package kepco.human.com;

public class Mabang {
	
	public void makeMabang() {
		int[][] mabang = new int[5][5];
		int x=0;
		int y=2;
		mabang[x][y] = 1;
		
		for(int pos=2; pos<=25; pos++) {
			x=x-1;
			y=y-1;
			
			if(x>0 && y>0 && mabang[x][y]==0) {
				mabang[x][y]=pos;
			}else if(x>0 && y>0 && mabang[x][y]!=0) {
				mabang[x+2][y+1]=pos;
			}else if(x<0 && y>0) {
				mabang[x+5][y]=pos;
			}else if(x>0 && y<0) {
				mabang[x][y+5]=pos;
			}else if(x<0 && y<0) {
				mabang[x+2][y+1]=pos;
			}
		}
		for(int[] temp : mabang) {
			for(int value:temp) {
				System.out.print(value+"  ");
			}
			System.out.println();
		}
			
	}
	
	public static void main(String[] args) {
		new Mabang().makeMabang();
	}

}
