#include <stdio.h>

void InsertionSort(int *array, int n){
    int i, j, key;
    for(i = 0; i < n; i++){
        key = array[i];
        j = i - 1;
        while(j >= 0 && array[j] > key){
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = key;
    }
}

int main(){
    int array[] = {4,2,3,1};
    int n = sizeof(array) / sizeof(array[0]);
    InsertionSort(array, n);
    for(int i = 0; i < n; i++){
        printf("%d, ", array[i]);
    }
}