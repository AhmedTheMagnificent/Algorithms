#include <stdio.h>

void swap(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

void WaveSort(int *array, int n){
    for(int i = 0; i < n; i += 2){
        if(i > 0 && array[i] > array[i - 1]){
            swap(&array[i], &array[i - 1]);
        }
        if(i < n - 1 && array[i] > array[i + 1]){
            swap(&array[i], &array[i + 1]);
        }
    }
}

int main(){
    int array[] = {4,2,3,1};
    int n = sizeof(array) / sizeof(array[0]);
    WaveSort(array, n);
    for(int i = 0; i < n; i++){
        printf("%d, ", array[i]);
    }
}
