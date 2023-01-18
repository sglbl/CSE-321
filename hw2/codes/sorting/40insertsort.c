#include <stdio.h>	 //insertion sort    ( kucukten buyuge )
#define MAX 50       //bubble sort tersi gibi. kucuk elemaný basa atiyor. ordan buluyor.
// 4 3 50 1 2
// (2.elemandan basla. 3 4ten kucuk mu?evetse 3ü sola al.)
// 3 4 50 1 2
// ilk ucu siralanmis. bak 1 50den kucuk mu? evetse devam et degilse tmm. 1 4ten kucuk mu?evet, sola kaydirmaya devam.

void insertionsort(int arr[],int size){
	int j, element;
	
	for(int i=1; i<size; i++){
		element = arr[i];
		j=i-1;
		while(j>= 0 && arr[j] > element){
			arr[j+1]=arr[j];      //to the left side.
			j--;
		}
		arr[j+1]=element;	
	}
}

int main(){	
	int i,array[MAX],size;
	printf("Kac elemanli: ");
	scanf("%d",&size);
	for(i=0;i<size;i++)
		scanf("%d",&array[i]);
	
	insertionsort(array,size);
	for(i=0;i<size;i++)
		printf("%d ",array[i]);

	return 0;
}