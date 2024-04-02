def MergeSort(array):
    if len(array) <= 1:
        return array
    else:
        left = mergesort(array[:len(array)//2])
        right = mergesort(array[len(array)//2:])
        sorted = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted.append(left[i])
                i+=1
            else:
                sorted.append(right[j])
                j+=1
        while i < len(left):
            sorted.append(left[i])
            i+=1
        while j < len(right):
            sorted.append(right[j])
            j+=1
        return sorted
    
