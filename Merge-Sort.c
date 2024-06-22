#include <stdio.h>

void Merge(int array[], int left[], int right[], int x, int y){
    int i, j, k;
    i = 0;
    j = 0;
    k = 0;
    while(i < x && j < y){
        if(left[i] < right[j]){
            array[k] = left[i];
            i++;
            k++;
        }
        else{
            array[k] = right[j];
            j++;
            k++;
        }
    }
    while(i < x){
        array[k] = left[i];
        i++;
        k++;
    }
    while(j < y){
        array[k] = right[j];
        j++;
        k++;
    }
}

void MergeSort(int array[], int n){
    if(n <= 1) return;
    int mid = n / 2;
    int left[mid], right[n - mid];
    for(int i = 0; i < mid; i++){
        left[i] = array[i];
        right[i] =  array[mid + i];
    }
    MergeSort(left, mid);
    MergeSort(right, n - mid);
    Merge(array, left, right, mid, n - mid);
}

int main(){
    int array[] = {4,2,3,1};
    int n = sizeof(array) / sizeof(array[0]);
    MergeSort(array, n);
    for(int i = 0; i < n; i++){
        printf("%d, ", array[i]);
    }
}