# LeetCode Notes:
# Problem: Sort an array of only 0s, 1s and 2s in-place.
# Idea: Keep 0s on the left, 2s on the right, and scan the middle.
# Trick: After swapping with high, do not move mid yet because the new value is still unchecked.
# Dry run: [1,2,1,0,2,0,1] -> push 0s left and 2s right -> [0,0,1,1,1,2,2].
# TC and SC: O(N) time because each value is handled once, O(1) space because only pointers are used.

# Brute force:
# Count 0s, 1s, 2s and overwrite the array.

def brute_force_sort_012(arr):
    """Sort 0s, 1s, 2s by counting (BRUTE FORCE)"""
    count_0 = 0
    count_1 = 0
    count_2 = 0
    
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1
    
    idx = 0
    
    for _ in range(count_0):
        arr[idx] = 0
        idx += 1
    
    for _ in range(count_1):
        arr[idx] = 1
        idx += 1
    
    for _ in range(count_2):
        arr[idx] = 2
        idx += 1
    
    return arr

# Test Brute Force
l1 = [1, 2, 1, 0, 2, 0, 1]
print("Brute Force Result:", brute_force_sort_012(l1.copy()))


# Optimal:
# Dutch National Flag with low, mid, high pointers.

def optimal_sort_012(arr):
    """Sort 0s, 1s, 2s using Dutch National Flag (OPTIMAL)"""
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# Test Optimal
l2 = [1, 2, 1, 0, 2, 0, 1]
print("Optimal Result:", optimal_sort_012(l2))

print("\nAdditional Tests:")
print("Array [0, 1, 2]:", optimal_sort_012([0, 1, 2]))
print("Array [2, 1, 0]:", optimal_sort_012([2, 1, 0]))
print("Array [2, 2, 2, 0, 0, 1]:", optimal_sort_012([2, 2, 2, 0, 0, 1]))
