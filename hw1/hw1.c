#include <stdio.h>
#include <stdlib.h>

int a(int array1[], int array2[], int n, int m){
	int max = 0;
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if(array1[i] * array2[j] > max)
				max = array1[i]*array2[j];
			
	return max;
}

int b(int array1[], int array2[], int n, int m){
	int *array3 = calloc(n+m, sizeof(int));

	for(int i = 0; i < n; i++){
		array3[i]   = array1[i];
	}
	for(int j = 0; j < m; j++){
		array3[n+j] = array2[j];
	}

	for(int i = 0; i < n + m; i++){
		for(int j = i+1; j < n + m; j++){
			if( array3[i] < array3[j] ){
				int temp = array3[i];
				array3[i] = array3[j];
				array3[j] = temp;
			}
		}
	}

	printf("B: ");
	for(int i=0; i < n + m; i++)
		printf("%d, ", array3[i]);
	printf("\n");			

}

int c(int array[], int n, int element){
	int *newArray = calloc(n+1, sizeof(int));
	for(int i = 0; i < n; i++)
		newArray[i] = array[i];
	newArray[n] = element;

	printf("C: ");
	for(int i=0; i < n+1; i++)
		printf("%d, ", newArray[i]);
	printf("\n");	
}

int d(int array[], int n, int elementToDelete){
	for(int i = 0; i < n; i++){
		if(array[i] == elementToDelete){
			
		}
	}
}

int main(){

	int array1[] = {13,8,3,4,5,7};
	int array2[] = {4,1,2,9,6,3, 11};

	int n = 6, m = 7;

	printf("A: %d\n", a(array1, array2, n, m));
	b(array1, array2, n, m);
	c(array1, n, 34);

	return 0;
}
