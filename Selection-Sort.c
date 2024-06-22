#include <stdio.h>

void SelectionSort(int array[], int n){
    int i, j, minindex, temp;
    for(i = 0; i < n; i++){
        minindex = i;
        for(j = i + 1; j < n; j++){
            if(array[minindex] > array[j]){
                minindex = j;
            }
        }
        temp = array[minindex];
        array[minindex] = array[i];
        array[i] = temp;
    }
}

int main(){
    int array[] = {4,2,3,1};
    int n = sizeof(array) / sizeof(array[0]);
    SelectionSort(array, n);
    for(int i = 0; i < n; i++){
        printf("%d, ", array[i]);
    }
}