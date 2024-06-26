def QuickSort(array):
    if len(array) <= 1:
        return array
    else:
        pi_index = partition(array)
        return QuickSort(array[:pi_index]) + [array[pi_index]] + QuickSort(array[pi_index + 1:])

def partition(array):
    pivot = array[0]
    i = j = 1
    while j < len(array):
        if array[j] > pivot:
            j += 1
        else:
            array[i], array[j] = array[j], array[i]
            i += 1
            j += 1
    i -= 1
    array[0], array[i] = array[i], array[0]
    return i

"""
    Quick Sort is a divide-and-conquer algorithm that selects a 'pivot' element from the array and partitions
    the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
    The sub-arrays are then sorted recursively.

    Steps:
    1. Choose a pivot element from the array.
    2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
    3. Recursively sort the sub-arrays.
    4. Combine the sorted sub-arrays and pivot into a single sorted array.

    Time Complexity:
    - Average: O(n log n), where n is the number of elements in the input array.
    - Worst-case: O(n^2), which occurs when the smallest or largest element is always chosen as the pivot.
    
    Space Complexity:
    - O(log n) for the recursive call stack in the average case.

    The sort is not stable, meaning equal elements may not retain their relative order.
    """