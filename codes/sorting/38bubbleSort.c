#include <stdio.h>     //Kucukten buyuge
#define MAX 50

void bubblesort(int arr[],int size){  // Size'i ayri parametre olarak gondermek zorundasin.
	int temp;

	for(int i=0; i<size; i++){
		for(int j=1; j<size-i; j++){
			if(arr[j-1] > arr[j] ){		//Yerlerini degistirme. (onceki eleman sonrakinden buyukse)
				temp=arr[j];
				arr[j]=arr[j-1];
				arr[j-1]=temp;
			}
		}
	}
	
}

int main(){
	int i,array[MAX],size;
	printf("Kac elemanli array istedigini yaz: ");
	scanf("%d",&size);
	for(i=0;i<size;i++)
		scanf("%d",&array[i]);
	
	bubblesort(array,size);
	
	for(i=0;i<size;i++)
		printf("%d ",array[i]);
	
	printf("\n");
	return 0;
}