#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int devuelve_longitud(char *pletra){
	int longitud=0;
	int cont=0;
	while(*(pletra+cont)!='\0'){
		cont++;
	}
	longitud=cont;
	return(longitud);
}
int main(){

	char *lista[3];
	int cont;
	char aux[20];
	int longitud;
	for(cont=0;cont<3;cont++){
		printf("\npalabra %d: ",cont);
		scanf("%s",aux);
		printf("\n longitud = %d",devuelve_longitud(aux));
		//lista[cont]=(char *) malloc(longitud);
		//strcpy(lista[cont],aux);
		
	}
	printf("\n**************************");
	printf("\n**    LISTA PALABRAS    **");
	printf("\n**************************");
	for(cont=0;cont<3;cont++){
		printf("\n %d .- %s",cont,*(lista+cont));
	}
	
	return 0;
}
