package MiCodigo;

public class ManejaAlumno {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Alumno manueh;
		AlumnoBecado Titi;
		Fecha nacimientoLolito;
		Fecha nacimientoTiti;
		nacimientoLolito=new Fecha(14,3,2021);
		nacimientoTiti=new Fecha(1,2,1988);
		pepe=new Alumno("Lolito","Fdez","García",nacimientoLolito);
		juana=new AlumnoBecado("Titi","Bustillo","Lopez",nacimientoTiti);
		System.out.println("Nuevo alumno: ");
		System.out.println(manueh.getNombre());
		System.out.println(manueh.getApellido1());
		System.out.println(manueh.getApellido2());
		System.out.println((manueh.getFechaNacimiento()).getFechaConFormatoLargo());
		System.out.println("Alumna becada");
		System.out.println(titi.getNombre());
		System.out.println(titi.getApellido1());
		System.out.println(titi.getApellido2());
		System.out.println((titi.getFechaNacimiento()).getFechaConFormatoLargo());
		System.out.println("żBecada?: "+titi.isBeca());
	}

}
