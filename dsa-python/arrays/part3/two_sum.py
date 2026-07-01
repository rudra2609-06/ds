# LeetCode Notes:
# Problem: Find indices of two different elements whose sum is equal to target.
# Idea: Store seen values in a hash map and look for target - current.
# Trick: Check the complement before storing current so the same index is not reused.
# Dry run: [2,6,5,8,11], target=14 -> at 8 we need 6, which was already seen at index 1.
# TC and SC: O(N) time because we scan once, O(N) space because the map stores seen values.

def brute_force_two_sum(arr, target):
    """Find two sum using nested loop (BRUTE FORCE)"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return [-1, -1]

# Test Brute Force
l1 = [2, 6, 5, 8, 11]
target = 14
print("Brute Force Result:", brute_force_two_sum(l1, target))


def optimal_two_sum(arr, target):
    """Find two sum using hash map (OPTIMAL)"""
    hash_map = {}
    
    for i in range(len(arr)):
        current_element = arr[i]
        complement = target - current_element
        
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[current_element] = i
    
    return [-1, -1]

# Test Optimal
l2 = [2, 6, 5, 8, 11]
target = 14
print("Optimal Result:", optimal_two_sum(l2, target))

print("\nAdditional Tests:")
print("Array [1, 5, 7, -1], target=6:", optimal_two_sum([1, 5, 7, -1], 6))
print("Array [3, 2, 4], target=6:", optimal_two_sum([3, 2, 4], 6))
print("Array [2, 7, 11, 15], target=9:", optimal_two_sum([2, 7, 11, 15], 9))
