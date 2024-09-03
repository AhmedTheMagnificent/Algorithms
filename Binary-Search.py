def BinarySearch(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
            
print(BinarySearch([1,1,2,3,3,5,5,6,7,8], 1))