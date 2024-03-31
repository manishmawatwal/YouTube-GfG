# n - length of the array
def convertToWave(n, a):
    # sort the array
    a.sort()

    # a loop to interchange the elements
    for i in range(0, n-1, 2):
        a[i+1], a[i] = a[i], a[i+1]
    return a

print(convertToWave(5, [1, 2, 3, 4, 5]))
