def CountingSort(arr):
    if len(arr) == 0:
        return arr
    maximum = max(arr) + 1
    countArray = [0] * maximum
    retArray = [0] * len(arr)
    for i in arr:
        countArray[i] += 1
    for i in range(1, maximum):
        countArray[i] += countArray[i-1] 
    for num in arr[::-1]:
        countArray[num] -= 1
        retArray[countArray[num]] = num
    return retArray