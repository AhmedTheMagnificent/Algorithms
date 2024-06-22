#include <stdio.h>

void BubbleSort(int array[], int n){
    int i, j, temp;
    for(i = 0; i < n; i++){
        for(j = i+1; j < n; j++){
            if(array[i] > array[j]){
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}

int main(){
    int array[] = {4,2,3,1};
    int n = sizeof(array) / sizeof(array[0]);
    BubbleSort(array, n);
    for(int i = 0; i < n; i++){
        printf("%d, ", array[i]);
    }
}