# LeetCode Notes:
# Problem: Remove duplicates from a sorted array in-place and return the count of unique values.
# Idea: Keep one pointer at the last unique value and another pointer to scan ahead.
# Trick: Because the array is sorted, a different value means a new unique value.
# Dry run: [1,1,2,2,4,5,6,6] -> write 2,4,5,6 after 1 -> first 5 values become [1,2,4,5,6].
# TC and SC: O(N) time because each element is checked once, O(1) space because we write inside the same array.

# Brute force:
# Remove duplicates one by one. This is slow because pop shifts elements.

def brute_force_remove_duplicates(arr):
    """Remove duplicates using brute force (multiple passes with removal)"""
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i + 1)
        else:
            i += 1
    return len(arr)

# Test Brute Force
l1 = [1, 1, 2, 2, 4, 5, 6, 6]
count = brute_force_remove_duplicates(l1.copy())
print(f"Brute Force - Unique count: {count}")


# Optimal:
# Move only new values to the next write position.

def optimal_remove_duplicates(arr):
    """Remove duplicates using two-pointer technique (OPTIMAL)"""
    if len(arr) == 0:
        return 0
    
    i = 0
    
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1

# Test Optimal
l2 = [1, 1, 2, 2, 4, 5, 6, 6]
count = optimal_remove_duplicates(l2)
print(f"Optimal - Unique count: {count}")
print(f"First {count} elements: {l2[:count]}")
