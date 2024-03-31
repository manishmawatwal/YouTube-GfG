# n - length of the array
def MissingNumber(array, n):
    # Calculate the expected sum of the first 'n' natural numbers
    expected_sum = (n*(n+1))//2

    # Calculate the actual sum of elements in the array
    actual_sum = sum(array)

    # The missing number is the difference between the expected and actual sums
    missing_number = expected_sum - actual_sum
    
    return missing_number

#Let's test our function
print("The missing number in the array is:", MissingNumber([1, 2, 3, 5], 5))