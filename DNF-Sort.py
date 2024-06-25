def DNFSort(array):
    low = 0
    mid = 0
    high = len(array) - 1
    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    return array

"""
    Dutch National Flag (DNF) Sort, also known as 3-way partitioning, is an efficient algorithm for sorting an array
    containing three distinct values. The algorithm was designed by Edsger W. Dijkstra, a Dutch computer scientist.

    Steps:
    1. Initialize three pointers:
        - 'low' points to the end of the sorted 0s section.
        - 'mid' points to the current element under consideration.
        - 'high' points to the beginning of the unsorted 2s section.
    2. Iterate through the array until 'mid' crosses 'high':
        - If the current element is 0:
            - Swap it with the element at index 'low'.
            - Increment both 'low' and 'mid'.
        - If the current element is 1:
            - Just increment 'mid'.
        - If the current element is 2:
            - Swap it with the element at index 'high'.
            - Decrement 'high'.
    3. Continue this process until 'mid' crosses 'high', ensuring that the elements are sorted into the three partitions.

    Time Complexity:
    - O(n), where n is the number of elements in the array.

    Space Complexity:
    - O(1), as it only requires a constant amount of additional space for the pointers.

    The algorithm is stable, meaning equal elements retain their relative order.
    """