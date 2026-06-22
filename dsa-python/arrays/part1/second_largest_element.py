'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                        FIND SECOND LARGEST ELEMENT IN ARRAY                    ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given an unsorted array of integers, find the second largest element.         ║
║ Handle edge cases: duplicates, negative numbers, single elements.             ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  [12, 11, 10, 9, 2]                                                  ║
║ • Output: 11 (largest=12, second_largest=11)                                  ║
║                                                                                ║
║ EDGE CASES:                                                                    ║
║ • Array with duplicates:     [5, 5, 5] → -1 (no distinct second largest)     ║
║ • Negative numbers:          [-5, -1, -10] → -5 (second largest)             ║
║ • Two elements:              [5, 3] → 3                                       ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Sort and Find
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N log N)  - Sorting dominates
# Space Complexity: O(1) or O(N) - Depends on sorting algorithm
#
# HOW IT WORKS:
# 1. Sort array in descending order
# 2. Iterate to find first element different from largest
# 3. That element is the second largest
#
# EXAMPLE: [12, 11, 10, 9, 2]
# After sorting: [12, 11, 10, 9, 2]
# arr[0]=12 (largest)
# arr[1]=11 (second_largest) ✓

def brute_force_second_largest(arr):
    """Find second largest using sorting (BRUTE FORCE)"""
    if len(arr) < 2:
        return -1
    
    # Sort in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # Find first element different from largest
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] != sorted_arr[0]:
            return sorted_arr[i]
    
    # All elements are same (all are largest)
    return -1

# Test Brute Force
l1 = [12, 11, 10, 9, 2]
print("Brute Force Result:", brute_force_second_largest(l1))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Single Pass with Two Variables
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(1)   - Only two variables
#
# HOW IT WORKS:
# 1. Initialize largest = first element, second_largest = -1
# 2. Iterate through remaining elements:
#    - If element > largest: update second_largest = largest, then largest = element
#    - Else if element > second_largest AND element ≠ largest: 
#      update second_largest = element
# 3. Continue until end
# 4. Return second_largest
#
# KEY LOGIC:
# • Maintain largest and second_largest variables
# • When we find new largest, old largest becomes second_largest
# • Only update second_largest if it's larger and not equal to largest
#
# EXAMPLE: [12, 11, 10, 9, 2]
# Start: largest=12, second_largest=-1
# 11: Is 11 > 12? No. Is 11 > -1 and 11≠12? Yes → second_largest=11
# 10: Is 10 > 12? No. Is 10 > 11 and 10≠12? No
# 9:  Is 9 > 12? No. Is 9 > 11 and 9≠12? No
# 2:  Is 2 > 12? No. Is 2 > 11 and 2≠12? No
# Result: second_largest = 11 ✓

def optimal_second_largest(arr):
    """Find second largest using single pass (OPTIMAL)"""
    if len(arr) < 2:
        return -1
    
    largest = arr[0]
    second_largest = -1
    
    for i in range(1, len(arr)):
        if arr[i] > largest:
            # New largest found, previous largest becomes second largest
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            # Update second largest if it's greater and different from largest
            second_largest = arr[i]
    
    # Return -1 if second_largest was never updated (all elements same)
    return second_largest

# Test Optimal
l2 = [12, 11, 10, 9, 2]
print("Optimal Result:", optimal_second_largest(l2))

# Additional test cases
print("\nAdditional Tests:")
print("Array [5, 5, 5]:", optimal_second_largest([5, 5, 5]))  # -1 (all same)
print("Array [-5, -1, -10]:", optimal_second_largest([-5, -1, -10]))  # -5
print("Array [3, 5]:", optimal_second_largest([3, 5]))  # 3


