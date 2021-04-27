package MiCodigo;

public class ManejaMascota {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Mascota Lionel;
		Lionel=new Mascota("Gato","Lionel",13);
		MascotaConCuidados Isco;
		Isco=new MascotaConCuidados("Dinosaurio","Isco",24);
		System.out.println("Mascota 1 ");
		System.out.println("Se llama: "+Lionel.getNombre());
		System.out.println("Es un: "+Lionel.getEspecie());
		System.out.println("Y tiene: "+Lionel.getEdad()+" años");
		System.out.println("Mascota 2 ");
		System.out.println("Se llama: "+Isco.getNombre());
		System.out.println("Es un: "+Isco.getEspecie());
		System.out.println("Y tiene: "+Isco.getEdad()+" años");
		Isco.setCuidados("Sacarlo a pasear");
		System.out.println("Cuidados especiales: "+Isco.getCuidados());
		
		
		
		
	}

}
