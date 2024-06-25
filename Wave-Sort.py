def WaveSort(array):
    for i in range(0,len(array), 2):
        if array[i] > array[i - 1] and i > 0:
            array[i], array[i - 1] = array[i - 1], array[i]
        if array[i] > array[i + 1] and i < len(array) - 1:
            array[i], array[i + 1] = array[i + 1], array[i]
    return array

"""
    Wave Sort is an algorithm that sorts an array into a wave-like pattern.
    In a wave sorted array, elements are ordered such that:
    arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] ...

    Steps:
    1. Traverse the array with step size 2 (i.e., check every other element).
    2. For each element at index i:
        - If the current element is smaller than the previous element, swap them.
        - If the current element is smaller than the next element, swap them.
    3. Continue this process for all elements to ensure the wave pattern.

    Time Complexity:
    - O(n), where n is the number of elements in the array.

    Space Complexity:
    - O(1), as it only requires a constant amount of additional space for the swaps.

    Parameters:
    - arr (list): List of integers to be wave sorted.

    Returns:
    - None: The array is sorted in-place.
    """


