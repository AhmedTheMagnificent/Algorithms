def RadixSort(array):
    for i in array:
    
    
def CountingSort(array):
    if len(array) == 0:
        return array
    maximum = max(array)
    countArray = [0] * maximum + 1
    retArray = [0] * len(array)
    for i in array:
        countArray[i] += 1
    for i in range(len(1,maximum)):
        countArray[i] += countArray[i-1]
    for num in array:
        countArray[num] -= 1
        retArray[countArray[num]] = num
    return retArray