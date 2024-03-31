def getMinMax(a):
    minimum_num = min(a)
    maximum_num = max(a)
    return minimum_num, maximum_num

print("(Minimum, Maximum) number in the array", getMinMax([3, 2, 1, 56, 10000, 167]))