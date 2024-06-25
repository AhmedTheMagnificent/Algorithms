#include <stdio.h>

void swap(int *x, int *y){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void DNFSort(int *array, int n){
    int low = 0, mid = 0, high = n - 1;
    while(mid <= high){
        if(array[mid] == 0){
            swap(&array[low], &array[mid]);
            low++;
            mid++;
        }
        else if(array[mid] == 1){
            mid++;
        }
        else{
            swap(&array[mid], &array[high]);
            high--;
        }
    }
}

int main(){
    int array[] = {2,1,0,0,2,2,1,2,0,1};
    int n = sizeof(array) / sizeof(array[0]);
    DNFSort(array, n);
    for(int i = 0; i < n; i++){
        printf("%d, ", array[i]);
    }
}