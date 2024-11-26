public class SelectionSort{
    public static void selectionSort(int array[]){
        int n = array.length;
        for(int i = 0; i < n; i++){
            int minIndex = i;
            for(int j = i; j < n; j++){
                if(array[j] < array[minIndex]){
                    minIndex = j;
                }
            }
            int temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }

    public static void main(String[] args) {
        int array[] = {64, 25, 12, 22, 11};
        selectionSort(array);
        for(int num : array){
            System.err.println(" " + num);
        }
    }

    
}