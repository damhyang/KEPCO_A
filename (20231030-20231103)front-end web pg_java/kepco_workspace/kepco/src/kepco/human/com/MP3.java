package kepco.human.com;

public class MP3 implements Elec{

	@Override
	public void VolumeUp() {
		System.out.println("MP3 볼륨업");
	}

	@Override
	public void VolumeDown() {
		System.out.println("MP3 볼륨다운");
	}
	
}
