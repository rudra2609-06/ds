# LeetCode Notes:
# Problem: Left rotate the array by d places, so the first d values move to the end.
# Idea: Reverse the first part, reverse the second part, then reverse the whole array.
# Trick: Three reversals place every value exactly where a left rotation needs it.
# Dry run: [1,2,3,4,5], d=2 -> [2,1,3,4,5] -> [2,1,5,4,3] -> [3,4,5,1,2].
# TC and SC: O(N) time because each value is touched a constant number of times, O(1) space because it is in-place.

# Brute force:
# Rotate by one step, d times.

def brute_force_left_rotate(arr, d):
    """Rotate array left by D positions using brute force"""
    d = d % len(arr)
    
    for _ in range(d):
        temp = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[len(arr) - 1] = temp
    
    return arr

# Test Brute Force
l1 = [1, 2, 3, 4, 5]
d = 2
print("Brute Force Result:", brute_force_left_rotate(l1.copy(), d))


def reverse(arr, low, high):
    """Helper function to reverse array elements from low to high index"""
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return arr

# Optimal:
# Reverse first d, reverse rest, reverse all.

def optimal_left_rotate(arr, d):
    """Rotate array left by D positions using reversal algorithm (OPTIMAL)"""
    d = d % len(arr)
    
    reverse(arr, 0, d - 1)
    reverse(arr, d, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)
    
    return arr

# Test Optimal
l2 = [1, 2, 3, 4, 5]
d = 2
print("Optimal Result:", optimal_left_rotate(l2.copy(), d))
