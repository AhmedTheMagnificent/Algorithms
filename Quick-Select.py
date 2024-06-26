def QuickSelect(arr, k):
    if len(arr) == 1:
        return arr[0]
    else:
        pi_index = partition(arr)
        numberOfElements = pi_index + 1
        if k == numberOfElements:
            return arr[pi_index]
        elif k < numberOfElements:
            return QuickSelect(arr[:pi_index], k)
        else:
            return QuickSelect(arr[pi_index+1:], k - numberOfElements)
        
def partition(arr):
    pivot = arr[0]
    i = j = 1
    while j < len(arr):
        if arr[j] > pivot:
            j += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    i -= 1
    arr[0], arr[i] = arr[i], arr[0]
    return i

"""
    QuickSelect is a selection algorithm to find the k-th smallest element in an unordered list.
    It is related to the QuickSort sorting algorithm.
    
    Steps:
    1. If the list contains only one element, return that element (base case).
    2. Otherwise, partition the list into elements less than and greater than a pivot.
    3. Determine the position of the pivot element in the sorted list.
    4. If the position of the pivot is the k-th element, return the pivot element.
    5. If k is less than the number of elements in the left sub-array, recursively call QuickSelect on the left sub-array.
    6. If k is greater, recursively call QuickSelect on the right sub-array, adjusting k to account for the elements in the left sub-array and the pivot.

    Time Complexity:
    - Average: O(n), where n is the number of elements in the input list.
    - Worst-case: O(n^2), which occurs when the pivot selection results in the most unbalanced partitions (e.g., always the smallest or largest element).

    Space Complexity:
    - O(log n) due to the recursive call stack in the average case.

    The algorithm is not stable, meaning the relative order of equal elements may not be preserved.
    """