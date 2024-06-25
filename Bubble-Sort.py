def BubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

"""
    Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements
    and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, indicating
    that the list is sorted.

    Steps:
    1. Start with the first element and compare it with the next element.
    2. If the first element is greater than the next element, swap them.
    3. Repeat this process for each pair of adjacent elements until the end of the list.
    4. Continue this process for multiple passes until no more swaps are needed.

    Time Complexity:
    - O(n^2) in the average and worst case, where n is the number of elements in the input array.
    - O(n) in the best case, which occurs when the array is already sorted.

    Space Complexity:
    - O(1), as it only requires a constant amount of additional space for the swapping.

    The sort is stable, meaning equal elements retain their relative order.
    """