package kepco.human.com;

import java.util.ArrayList;

public class GenericTest {
	ArrayList<Elec> human;
	
	public void test() {
//		ArrayList<Elec> human = new ArrayList<Elec>();
		  //제네릭을 이용해서 upcasting하는 방법
		//ArrayList<Elec> human = new ArrayList();
		human = new ArrayList();
		human.add(new MP3());
		human.add(new TV());
		human.add(new Radio());
		//익명클래스 활용 :클래스로 만드는 이유는 여러번 쓰기 때문인데 여러번 쓰지 않으면 클래스를 만들지 않고 이름이 없는 익명클래스를 만들어 한번만 쓴다.
		human.add(new Elec(){  //인터페이스는 추상메소드를 가져서 인스턴스가 될 수 없다. 따라서 인터페이스의 메소드를 오버라이딩하여 메소드를 추상메소드가 아니게 넣어준다.
			@Override
			public void VolumeUp() {
				System.out.println("cellphone 볼륨업");
			}

			@Override
			public void VolumeDown() {
				System.out.println("cellphone 볼륨다운");
			}  //이름이 없는 객체가 생성되어 "cellphone 볼륨업" "cellphone 볼륨다운"이 동작된다. 이 코드가 끝나면 다시 불러 쓸 수 없다.
 
		});
		
		System.out.println(human.size());
//		Object 클래스에 있는 toSAtring() 메소드는 println()을 만나면 자동으로 실행됨.
		System.out.println(human); //MP3에는 toString메소드가 없지만 부모인 toString의 메소드를 가져온다.
		System.out.println(new MP3());  //arraylist의 toString은 object 밑 abstractcollection 클래스에 오버라이딩이 되어 그 메소드를 당겨온다.
	}
	
	public void result() {
		for (int i=0; i<human.size(); i++) {  //test메소드 안에 human이 있기 때문에에러가 뜨므로 메소드 밖으로 빼냄.
			human.get(i).VolumeUp();
			human.get(i).VolumeDown();
		}

		System.out.println("-------------------------");
		
	//	향상된 for문()
		//for(:human)()
		for(Elec temp : human) {
		temp.VolumeUp();
		temp.VolumeDown();
		}
		
		System.out.println("-------------------------");
		int j=0;
		while(j<human.size()) {
			human.get(j).VolumeUp();
			human.get(j).VolumeDown();
			j++;
		}

	}
}
