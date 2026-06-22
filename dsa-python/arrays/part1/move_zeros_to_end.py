'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                         MOVE ALL ZEROS TO END OF ARRAY                         ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given an array with mixed zero and non-zero elements, move all zeros to the   ║
║ end while maintaining the relative order of non-zero elements.                ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  [1, 0, 2, 3, 0, 4, 0, 1]                                            ║
║ • Output: [1, 2, 3, 4, 1, 0, 0, 0]                                            ║
║                                                                                ║
║ KEY OBSERVATIONS:                                                              ║
║ • Non-zero elements should maintain their relative order (stable)             ║
║ • All zeros should be grouped at the end                                      ║
║ • Modify array in-place (no extra space for result array)                     ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Separate and Combine
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Multiple passes through array
# Space Complexity: O(N)   - Need temporary array for non-zeros
#
# HOW IT WORKS:
# 1. Count zeros in array
# 2. Extract all non-zero elements into new array
# 3. Append zeros to end
#
# STEPS FOR [1,0,2,3,0,4,0,1]:
# Step 1 - Count zeros: 3
# Step 2 - Non-zeros:   [1,2,3,4,1]
# Step 3 - Add zeros:   [1,2,3,4,1,0,0,0]

def brute_force_move_zeros(arr):
    """Move zeros to end using brute force approach"""
    zeros_count = 0
    
    # Count zeros
    for element in arr:
        if element == 0:
            zeros_count += 1
    
    # Extract non-zero elements
    result = []
    for element in arr:
        if element != 0:
            result.append(element)
    
    # Append zeros
    while zeros_count > 0:
        result.append(0)
        zeros_count -= 1
    
    return result

# Test Brute Force
l1 = [1, 0, 2, 3, 0, 4, 0, 1]
print("Brute Force Result:", brute_force_move_zeros(l1))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Two-Pointer In-Place Swap
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(1)   - In-place, no extra space
#
# HOW IT WORKS:
# 1. Find first zero element and store index in leftPointer
# 2. Scan rest of array with rightPointer
# 3. Whenever we find non-zero at rightPointer, swap with leftPointer position
# 4. Increment leftPointer to next position
#
# LOGIC:
# • leftPointer marks position where next non-zero should go
# • rightPointer scans for non-zero elements
# • When found, swap and move leftPointer forward
#
# EXAMPLE: [1,0,2,3,0,4,0,1]
# L marks leftPointer, R marks rightPointer
# [1,L,2,3,0,4,0,1]  → [1,2,L,3,0,4,0,1]  → [1,2,3,L,0,4,0,1]
# [1,2,3,L,0,4,0,1]  → [1,2,3,4,L,0,0,1]  → [1,2,3,4,1,L,0,0]
# Result: [1,2,3,4,1,0,0,0] ✓

def optimal_move_zeros(arr):
    """Move zeros to end using two-pointer in-place technique (OPTIMAL)"""
    leftPointer = -1
    
    # Find first zero
    for i in range(len(arr)):
        if arr[i] == 0:
            leftPointer = i
            break
    
    # If no zero found, array is already correct
    if leftPointer == -1:
        return arr
    
    # Use rightPointer to find non-zeros and swap
    for rightPointer in range(leftPointer + 1, len(arr)):
        if arr[rightPointer] != 0:
            # Swap non-zero element to leftPointer position
            arr[rightPointer], arr[leftPointer] = arr[leftPointer], arr[rightPointer]
            leftPointer += 1
    
    return arr

# Test Optimal
l2 = [1, 0, 2, 3, 0, 4, 0, 1]
print("Optimal Result:", optimal_move_zeros(l2))









	


