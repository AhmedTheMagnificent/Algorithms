def CountingSort(array):
    if len(array) == 0:
        return array
    maximum = max(array) + 1
    countArray = [0] * maximum
    retArray = [0] * len(array)
    for i in array:
        countArray[i] += 1
    for i in range(1, maximum):
        countArray[i] += countArray[i-1] 
    for num in array[::-1]:
        countArray[num] -= 1
        retArray[countArray[num]] = num
    return retArray

"""
    Counting Sort is a non-comparative sorting algorithm that sorts integers within a specific range.
    It works by counting the occurrences of each unique value in the input array, then uses this information
    to place each value in its correct position in the output array.

    Steps:
    1. Find the maximum value in the input array to determine the size of the count array.
    2. Initialize a count array with zeros, where the index represents elements from the input array.
    3. Count each element in the input array and store the count at the corresponding index in the count array.
    4. Modify the count array such that each element at each index stores the sum of previous counts.
       This helps in placing elements directly into their correct position in the output array.
    5. Iterate over the input array in reverse order to maintain stability (i.e., equal elements maintain their relative order).
    6. For each element, decrement the count in the count array and place the element in the output array at the position
       indicated by the count array.

    Time Complexity:
    - O(n + k), where n is the number of elements in the input array and k is the range of the input.

    Space Complexity:
    - O(n + k), due to the input array, count array, and output array.
    """
    