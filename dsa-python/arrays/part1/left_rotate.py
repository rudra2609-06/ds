'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                         LEFT ROTATE ARRAY BY D PLACES                          ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Rotate an array to the left by D positions. After rotation, first D elements  ║
║ should move to the end, and remaining elements shift left.                    ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  arr = [1, 2, 3, 4, 5], D = 2                                        ║
║ • Output: [3, 4, 5, 1, 2]                                                      ║
║                                                                                ║
║ KEY OBSERVATIONS:                                                              ║
║ • Rotation by D is same as rotation by D % N (where N = array size)           ║
║ • Left rotation moves leftmost element to the end, rest shift left            ║
║ • Need to handle cases where D > N using modulo operation                     ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Rotate one step at a time, D times
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(D * N) - D rotations, each taking O(N) time
# Space Complexity: O(1)     - Only using constant extra space
# 
# HOW IT WORKS:
# For each of D rotations:
#   1. Save first element in temp
#   2. Shift all elements one position to left
#   3. Place temp at the end
# 
# Example: [1,2,3,4,5], D=2
# Step 1: [2,3,4,5,1] (moved 1 to end)
# Step 2: [3,4,5,1,2] (moved 2 to end)

def brute_force_left_rotate(arr, d):
    """Rotate array left by D positions using brute force"""
    d = d % len(arr)  # Handle cases where d > n
    
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


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Reversal Algorithm (3-step reversal)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)     - Three passes through array
# Space Complexity: O(1)     - Only swapping, no extra space
#
# HOW IT WORKS:
# The key insight: Rotating left by D is equivalent to:
#   1. Reverse first D elements:     [1,2,3,4,5] → [3,2,1,4,5]
#   2. Reverse remaining N-D:        [3,2,1,4,5] → [3,2,1,5,4]
#   3. Reverse entire array:         [3,2,1,5,4] → [4,5,1,2,3]
# 
# WHY THIS WORKS:
# When you reverse subarrays strategically, elements naturally shift to new positions
#
# Example: [1,2,3,4,5], D=2
# Step 1 - Reverse [0:2]:   [2,1,3,4,5]
# Step 2 - Reverse [2:5]:   [2,1,5,4,3]
# Step 3 - Reverse [0:5]:   [3,4,5,1,2] ✓

def reverse(arr, low, high):
    """Helper function to reverse array elements from low to high index"""
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return arr

def optimal_left_rotate(arr, d):
    """Rotate array left by D positions using reversal algorithm (OPTIMAL)"""
    d = d % len(arr)
    
    # Step 1: Reverse first D elements
    reverse(arr, 0, d - 1)
    
    # Step 2: Reverse remaining elements
    reverse(arr, d, len(arr) - 1)
    
    # Step 3: Reverse entire array
    reverse(arr, 0, len(arr) - 1)
    
    return arr

# Test Optimal
l2 = [1, 2, 3, 4, 5]
d = 2
print("Optimal Result:", optimal_left_rotate(l2.copy(), d))



