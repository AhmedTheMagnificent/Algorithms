def SelectionSort(array):
    for i in range(len(array) - 1):
        minIndex = i
        for j in range(minIndex + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array 

"""
    Selection Sort is an in-place comparison sorting algorithm. It has an O(n^2) time complexity, making it inefficient
    on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity
    and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory
    is limited.

    Steps:
    1. Iterate over the array to find the minimum element in the unsorted part of the array.
    2. Swap the found minimum element with the first element of the unsorted part.
    3. Move the boundary of the sorted and unsorted part one element to the right.
    4. Repeat the process for the remaining unsorted part of the array.

    Time Complexity:
    - O(n^2), where n is the number of elements in the input array.
    
    Space Complexity:
    - O(1), as it only requires a constant amount of additional space.

    The sort is not stable, meaning equal elements may not retain their relative order.
    """