#include <stdio.h>   //selection sort   (kucukten buyuge)
//bubble sort tersi gibi. kucuk elemani basa atiyor. ordan buluyor.

void selectionsort(int arr[],int size){
	int temp, minIndex;

	for(int i=0; i<size; i++){
		minIndex = i; 
		for(int j=i+1; j<size; j++){
			if (arr[j] < arr[minIndex])
				minIndex=j; 
		}
		temp = arr[i];      // putting small element in the beginning.
		arr[i]=arr[minIndex];
		arr[minIndex]=temp;	
	}

}

int main(){	
	int i,array[50],size;
	printf("Kac elemanli: ");
	scanf("%d",&size);
	for(i=0;i<size;i++)
		scanf("%d",&array[i]);
	
	selectionsort(array,size);
	for(i=0;i<size;i++)
		printf("%d ",array[i]);
	printf("\n");
	return 0;
}