#include <stdio.h>

int partition(int *arr, int n, int low, int high){
    int pivot = arr[low];
    int temp;
    int i = 1;
    int j = 1;
    while(j <= high){
        if(arr[j] < pivot){
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j++;
        }
        else{
            j++;
        }
    }
    i--;
    temp = arr[0];
    arr[0] = arr[i];
    arr[i] = temp;
    return i;
}

void Quicksort(int *arr, int n, int low, int high){
    if(n <= 1){
        return;
    }
    int pi_index= partition(arr, n, low, high);
    Quicksort(arr, n, 0, pi_index);
    Quicksort(arr, n, pi_index, n);
}