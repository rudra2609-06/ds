# LeetCode Notes:
# Problem: Move all zeroes to the end and keep the order of non-zero values same.
# Idea: Find the first zero, then swap every later non-zero into that place.
# Trick: The left pointer always tells where the next non-zero should go.
# Dry run: [1,0,2,3,0,4,0,1] -> move 2,3,4,1 forward -> [1,2,3,4,1,0,0,0].
# TC and SC: O(N) time because each index is visited once, O(1) space because swaps happen in-place.

# Brute force:
# Make a new list of non-zero values, then add all zeroes at the end.

def brute_force_move_zeros(arr):
    """Move zeros to end using brute force approach"""
    zeros_count = 0
    
    for element in arr:
        if element == 0:
            zeros_count += 1
    
    result = []
    for element in arr:
        if element != 0:
            result.append(element)
    
    while zeros_count > 0:
        result.append(0)
        zeros_count -= 1
    
    return result

# Test Brute Force
l1 = [1, 0, 2, 3, 0, 4, 0, 1]
print("Brute Force Result:", brute_force_move_zeros(l1))


# Optimal:
# Swap each non-zero with the first zero position seen so far.

def optimal_move_zeros(arr):
    """Move zeros to end using two-pointer in-place technique (OPTIMAL)"""
    leftPointer = -1
    
    for i in range(len(arr)):
        if arr[i] == 0:
            leftPointer = i
            break
    
    if leftPointer == -1:
        return arr
    
    for rightPointer in range(leftPointer + 1, len(arr)):
        if arr[rightPointer] != 0:
            arr[rightPointer], arr[leftPointer] = arr[leftPointer], arr[rightPointer]
            leftPointer += 1
    
    return arr

# Test Optimal
l2 = [1, 0, 2, 3, 0, 4, 0, 1]
print("Optimal Result:", optimal_move_zeros(l2))
