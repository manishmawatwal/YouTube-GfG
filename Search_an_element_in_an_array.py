# arr - array in which element has to be searched
# X - element which has to be searched
def search(arr, X):
    if X in arr:
        return arr.index(X)
    else:
        return -1

print(search([1, 2, 3, 4, 5], 4))