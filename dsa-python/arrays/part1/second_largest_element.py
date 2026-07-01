# LeetCode Notes:
# Problem: Find the second largest distinct value in the array. If it does not exist, return -1.
# Idea: Scan once and keep track of the largest and second largest values.
# Trick: When a new largest comes, the old largest becomes the second largest.
# Dry run: [12,11,10,9,2] -> largest=12, second=11, rest stay smaller, so answer is 11.
# TC and SC: O(N) time because we scan once, O(1) space because only two variables are used.

# Brute force:
# Sort in reverse order and return the first value different from the largest.

def brute_force_second_largest(arr):
    """Find second largest using sorting (BRUTE FORCE)"""
    if len(arr) < 2:
        return -1
    
    sorted_arr = sorted(arr, reverse=True)
    
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[0]:
            return sorted_arr[i]
    
    return -1

# Test Brute Force
l1 = [12, 11, 10, 9, 2]
print("Brute Force Result:", brute_force_second_largest(l1))


# Optimal:
# Keep largest and second_largest while moving left to right.

def optimal_second_largest(arr):
    """Find second largest using single pass (OPTIMAL)"""
    if len(arr) < 2:
        return -1
    
    largest = arr[0]
    second_largest = -1
    
    for i in range(1, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    
    return second_largest

# Test Optimal
l2 = [12, 11, 10, 9, 2]
print("Optimal Result:", optimal_second_largest(l2))

# Additional test cases
print("\nAdditional Tests:")
print("Array [5, 5, 5]:", optimal_second_largest([5, 5, 5]))
print("Array [-5, -1, -10]:", optimal_second_largest([-5, -1, -10]))
print("Array [3, 5]:", optimal_second_largest([3, 5]))
