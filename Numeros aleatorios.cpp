/*

Haz un juego en el que compites con el ordenador. TReglas:
1. Se tira el dado(n aleatorio) 3 veces de forma consecutiva
> TURNO 1. ORDENADOR (presiona cualquier tecla para tirar el dado)
> 4
> TURNO 1. PLAYER H (presiona cualquier tecla para tirar el dado)
> 3
> Gana el ordenador ;)
> TURNO 2.
Al final se dan todos los resultados parciales, la suma de los puntos
y se proclama el ganador.
*/
#include<stdio.h>
#include<stdlib.h>
#include<time.h>


int main(){
	int puntuacion;
	int cont;
	int resultados[6];
	srand(time(0));
	for(cont=1;cont<=6000;cont++){
		puntuacion=rand()%6+1;	
		resultados[puntuacion-1]=resultados[puntuacion-1]+1;
	}
	//Muestro los resultados
	for(cont=0;cont<6;cont++){
		printf("resultados[%d]=%d\n",cont,resultados[cont]);
	}
	printf("%d",puntuacion);
	return 0;
}
