'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                            TWO SUM PROBLEM                                     ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given an array and a target sum, find indices of TWO DISTINCT elements that   ║
║ add up to the target. Return the indices (not values).                        ║
║                                                                                ║
║ ASSUMPTIONS:                                                                   ║
║ • Exactly one solution exists (exactly two numbers that sum to target)        ║
║ • Cannot use the same element twice (indices must be different)               ║
║ • Array indices are 1-indexed (some problems) or 0-indexed                    ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  arr = [2, 6, 5, 8, 11], target = 14                                ║
║ • Output: [1, 3] (arr[1]=6 + arr[3]=8 = 14)                                  ║
║ (or [6, 8] if returning values instead of indices)                           ║
║                                                                                ║
║ KEY INSIGHT:                                                                   ║
║ • For each element, check if (target - element) exists in hash map            ║
║ • Use hash map for O(1) lookup instead of searching with nested loop         ║
║ • Store element → index mapping in hash map as you go                        ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Nested Loop (Check All Pairs)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N²)   - All pairs of elements
# Space Complexity: O(1)    - No extra space
#
# HOW IT WORKS:
# 1. For each element at index i
# 2. For each element at index j where j > i
# 3. Check if arr[i] + arr[j] == target
# 4. If yes, return [i, j]
#
# PROBLEM:
# • Very slow! O(N²) for large arrays
# • Wasteful: repeatedly calculating (target - element)
#
# EXAMPLE: [2, 6, 5, 8, 11], target=14
# i=0: 2 + 6=8, 2 + 5=7, 2 + 8=10, 2 + 11=13 (no match)
# i=1: 6 + 5=11, 6 + 8=14 ✓ (found! indices 1,3)

def brute_force_two_sum(arr, target):
    """Find two sum using nested loop (BRUTE FORCE)"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    
    return [-1, -1]  # Not found

# Test Brute Force
l1 = [2, 6, 5, 8, 11]
target = 14
print("Brute Force Result:", brute_force_two_sum(l1, target))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Hash Map (One-Pass)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(N)   - Hash map stores up to N elements
#
# HOW IT WORKS:
# 1. Create empty hash map to store {element: index}
# 2. Iterate through array
# 3. For each element, calculate complement = target - current_element
# 4. Check if complement exists in hash map:
#    - If YES: found the pair! Return current_index and stored_index
#    - If NO: store current_element → current_index in hash map
# 5. Continue until found
#
# WHY THIS WORKS:
# • Hash map gives O(1) lookup time
# • No nested loops = O(N) instead of O(N²)
# • Store previous elements as we scan (only store once)
#
# EXAMPLE: [2, 6, 5, 8, 11], target=14
# 
# Initial: hash_map = {}, complement_needed = 14
# 
# i=0: current=2
#      complement = 14-2 = 12
#      12 in hash_map? No
#      Store: hash_map = {2: 0}
# 
# i=1: current=6
#      complement = 14-6 = 8
#      8 in hash_map? No
#      Store: hash_map = {2: 0, 6: 1}
# 
# i=2: current=5
#      complement = 14-5 = 9
#      9 in hash_map? No
#      Store: hash_map = {2: 0, 6: 1, 5: 2}
# 
# i=3: current=8
#      complement = 14-8 = 6
#      6 in hash_map? YES! At index 1
#      Return [1, 3] ✓

def optimal_two_sum(arr, target):
    """Find two sum using hash map (OPTIMAL)"""
    hash_map = {}  # {element: index}
    
    for i in range(len(arr)):
        current_element = arr[i]
        complement = target - current_element
        
        # Check if complement exists in hash map
        if complement in hash_map:
            # Found the pair!
            return [hash_map[complement], i]
        
        # Store current element with its index
        hash_map[current_element] = i
    
    # Not found
    return [-1, -1]

# Test Optimal
l2 = [2, 6, 5, 8, 11]
target = 14
print("Optimal Result:", optimal_two_sum(l2, target))

# Additional test cases
print("\nAdditional Tests:")
print("Array [1, 5, 7, -1], target=6:", optimal_two_sum([1, 5, 7, -1], 6))  # [1,2] or [3,1]
print("Array [3, 2, 4], target=6:", optimal_two_sum([3, 2, 4], 6))  # [1,2]
print("Array [2, 7, 11, 15], target=9:", optimal_two_sum([2, 7, 11, 15], 9))  # [0,1]



