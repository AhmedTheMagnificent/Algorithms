def MergeSort(array):
    if len(array) <= 1:
        return array
    else:
        left = MergeSort(array[:len(array)//2])
        right = MergeSort(array[len(array)//2:])
        sorted = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted.append(left[i])
                i+=1
            else:
                sorted.append(right[j])
                j+=1
        while i < len(left):
            sorted.append(left[i])
            i+=1
        while j < len(right):
            sorted.append(right[j])
            j+=1
        return sorted
    
"""
    Merge Sort is a divide-and-conquer algorithm that recursively divides the input array into halves
    until each subarray contains a single element, then merges the subarrays to produce a sorted array.

    Steps:
    1. Divide the array into two halves.
    2. Recursively sort each half.
    3. Merge the two sorted halves into a single sorted array.

    Time Complexity:
    - O(n log n), where n is the number of elements in the input array.
    
    Space Complexity:
    - O(n), due to the additional space required for the temporary arrays used during the merge process.

    The merge process ensures stability, as it preserves the relative order of equal elements.
    """