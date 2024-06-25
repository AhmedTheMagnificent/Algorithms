#include <stdio.h>
#include <stdlib.h>

int max(int *array, int n){
    int max = array[0];
    for(int i = 1; i < n; i++){
        if(max < array[i]){
            max = array[i];
        }
    }
    return max + 1;
}

int *CountingSort(int *array, int n){
    int maximum = max(array, n);
    int *countArray = (int *)malloc(sizeof(int) * maximum);
    int *retArray = (int *)malloc(sizeof(int) * n);
    for(int i = 0; i < maximum; i++){
        countArray[i] = 0;
    }
    for(int i = 0; i < n; i++){
        countArray[array[i]]++;
    }
    for(int i = 1; i < maximum; i++){
        countArray[i] += countArray[i - 1];
    }
    for(int i = n - 1; i >= 0; i--){
        countArray[array[i]]--;
        retArray[countArray[array[i]]] = array[i];
    }
    free(countArray);
    return retArray;
}

int main(){
    int array[] = {4,2,3,1};
    int n = sizeof(array) / sizeof(array[0]);
    int *sortedArray = CountingSort(array, n);
    for(int i = 0; i < n; i++){
        printf("%d, ", sortedArray[i]);
    }
}