def isAnagram(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

print("Check whether the given strings are anagram:", isAnagram("geeksforgeeks", "forgeeksgeeks"))