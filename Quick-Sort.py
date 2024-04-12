def QuickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array if x < pivot]
        right = [x for x in array if x > pivot]
        middle = [x for x in array if x == pivot]
        return QuickSort(left) + middle + QuickSort(right)