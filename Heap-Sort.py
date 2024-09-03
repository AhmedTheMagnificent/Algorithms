def heapify(array, n, i):
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
    if left < n and array[left] > array[largest]:
        largest = left
    if right < n and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def HeapSort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)
    return array


"""
    HeapSort is a comparison-based sorting algorithm that uses a binary heap data structure.

    Steps:
    1. Build a max heap from the input array. This ensures that the largest element is at the root.
    2. Swap the root (maximum value) with the last element of the array, then reduce the size of the heap by one.
    3. Heapify the root to restore the max-heap property.
    4. Repeat steps 2-3 until the entire array is sorted.

    Time Complexity:
    - O(n log n), where n is the number of elements in the input array. The heapify operation takes O(log n) and it is called n times.

    Space Complexity:
    - O(1), as HeapSort is an in-place sorting algorithm, meaning it requires no extra space for sorting the array.
    """

