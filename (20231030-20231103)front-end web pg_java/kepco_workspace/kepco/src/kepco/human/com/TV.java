package kepco.human.com;

public class TV implements Elec{

	@Override
	public void VolumeUp() {
		System.out.println("TV 볼륨업");
	}

	@Override
	public void VolumeDown() {
		System.out.println("TV 볼륨다운");
	}

}
