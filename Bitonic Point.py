def findMaximum(arr, n):
    low, high = 0, n-1
    while low < high:
        # calculate the middle index
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid]
        
        #if the right neighbor is smaller, search left.
        if arr[mid] > arr[mid + 1]:
            high = mid
            
        #if the right neighbor is larger, search right
        else:
            low = mid + 1
    return arr[n - 1]


print("Maximum element in the array:",findMaximum([1, 15, 25, 27, 42, 21, 17, 12, 11], 9))