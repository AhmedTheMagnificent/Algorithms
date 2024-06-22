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
    array[0], array[i - 1] = array[i - 1], array[0]
    return i - 1

