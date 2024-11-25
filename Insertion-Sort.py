def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

arr = [5,4,3,2,1]
new = InsertionSort(arr)

"""
    Insertion Sort is a simple and efficient comparison-based sorting algorithm. It builds the final sorted array one item
    at a time, with the input elements being taken one by one and inserted into their correct position.

    Steps:
    1. Start with the first element, considering it as sorted.
    2. Take the next element and insert it into the sorted portion of the array by shifting the elements that are greater
       to the right.
    3. Repeat the process for all elements until the entire array is sorted.

    Time Complexity:
    - O(n^2) in the average and worst case, where n is the number of elements in the input array.
    - O(n) in the best case, which occurs when the array is already sorted.
    
    Space Complexity:
    - O(1), as it only requires a constant amount of additional space.

    The sort is stable, meaning equal elements retain their relative order.
    """
    