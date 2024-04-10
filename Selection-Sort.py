def SelectionSort(array):
    for i in range(len(array) - 1):
        minIndex = i
        for j in range(minIndex + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array 
