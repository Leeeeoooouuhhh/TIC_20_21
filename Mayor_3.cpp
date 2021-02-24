/*
Números aleatorios

*/
#include<stdio.h>



int main(){
	int num1,num2,num3;
	printf("Introduce 3 numeros enteros:\n");
	printf("numero 1: ");
	scanf("%d",&num1);
	printf("numero 2: ");
	scanf("%d",&num2);
	printf("numero 3: ");
	scanf("%d",&num3);
	printf("El mayor de %d,%d y %d: ",num1,num2,num3);
	printf("%d",devuelve_mayor(num1,num2,num3));
	return 0;


