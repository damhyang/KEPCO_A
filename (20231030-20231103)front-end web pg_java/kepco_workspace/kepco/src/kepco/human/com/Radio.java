package kepco.human.com;

public class Radio implements Elec{

	@Override
	public void VolumeUp() {
		System.out.println("Radio 볼륨업");
	}

	@Override
	public void VolumeDown() {
		System.out.println("Radio 볼륨다운");
	}
	
}
