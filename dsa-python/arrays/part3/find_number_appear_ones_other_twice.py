'''
╔════════════════════════════════════════════════════════════════════════════════╗
║              FIND SINGLE NUMBER (OTHERS APPEAR TWICE)                          ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given an unsorted array where every element appears exactly twice except      ║
║ for ONE element that appears exactly once. Find that single element.          ║
║                                                                                ║
║ CONSTRAINTS & KEY OBSERVATIONS:                                               ║
║ • Array is UNSORTED (can be in any order)                                     ║
║ • All elements appear exactly 2 times EXCEPT one                             ║
║ • That one element appears exactly 1 time (find it!)                         ║
║ • Array contains positive integers                                           ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  arr = [1, 1, 2, 3, 3, 4, 4]                                        ║
║ • Output: 2 (only number appearing once)                                      ║
║                                                                                ║
║ WHY THIS IS ELEGANT:                                                           ║
║ • XOR is perfect for this problem (no other algorithm is simpler)            ║
║ • XOR Property: a ^ a = 0 (pair cancels out)                                 ║
║ • XOR Property: a ^ 0 = a (single element remains)                           ║
║ • XOR all elements and duplicates disappear, single remains!                 ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Hash Map / Frequency Count
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Two passes (one for counting, one for finding)
# Space Complexity: O(N)   - Hash map stores all unique elements
#
# HOW IT WORKS:
# 1. Count frequency of each element using hash map
# 2. Iterate through hash map and find element with frequency 1
#
# DISADVANTAGE:
# • Uses O(N) extra space
# • Not as elegant as XOR
#
# EXAMPLE: [1, 1, 2, 3, 3, 4, 4]
# Frequency: {1: 2, 2: 1, 3: 2, 4: 2}
# Find element with frequency 1 → 2 ✓

def brute_force_single_number(arr):
    """Find single number using hash map (BRUTE FORCE)"""
    freq_map = {}
    
    # Count frequencies
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Find element with frequency 1
    for num, freq in freq_map.items():
        if freq == 1:
            return num
    
    return -1

# Test Brute Force
l1 = [1, 1, 2, 3, 3, 4, 4]
print("Brute Force Result:", brute_force_single_number(l1))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - XOR (The Elegant Solution)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(1)   - Only one variable needed!
#
# HOW IT WORKS:
# 1. XOR all elements together
# 2. Duplicate pairs cancel out to 0 (because a ^ a = 0)
# 3. Result is the single element that appeared once
#
# WHY XOR IS PERFECT FOR THIS PROBLEM:
# 
# XOR PROPERTIES (The Magic):
# • Property 1: a ^ a = 0 (any number XOR itself = 0)
# • Property 2: a ^ 0 = a (any number XOR 0 = itself)
# • Property 3: XOR is commutative: a ^ b = b ^ a
# • Property 4: XOR is associative: (a ^ b) ^ c = a ^ (b ^ c)
#
# EXAMPLE: [1, 1, 2, 3, 3, 4, 4]
# Step by step:
#   xor = 0
#   xor = 0 ^ 1 = 1
#   xor = 1 ^ 1 = 0
#   xor = 0 ^ 2 = 2
#   xor = 2 ^ 3 = 1 (binary: 010 ^ 011 = 001)
#   xor = 1 ^ 3 = 2 (binary: 001 ^ 011 = 010)
#   xor = 2 ^ 4 = 6 (binary: 010 ^ 100 = 110)
#   xor = 6 ^ 4 = 2 (binary: 110 ^ 100 = 010)
# 
# Wait, that doesn't look right. Let me trace more carefully:
# xor = 0
# xor ^= 1 → xor = 1
# xor ^= 1 → xor = 0 (1 ^ 1 = 0)
# xor ^= 2 → xor = 2 (0 ^ 2 = 2)
# xor ^= 3 → xor = 1 (2 ^ 3 = 1)
# xor ^= 3 → xor = 2 (1 ^ 3 = 2)
# xor ^= 4 → xor = 6 (2 ^ 4 = 6)
# xor ^= 4 → xor = 2 (6 ^ 4 = 2) ✓ Correct!
#
# THE LOGIC:
# 1 ^ 1 = 0        (first pair cancels)
# 0 ^ 2 = 2        (single element remains)
# 2 ^ 3 = 1        (accumulating)
# 1 ^ 3 = 2        (second pair 3^3 part cancels: 2^3^3 = 2)
# 2 ^ 4 = 6        (accumulating)
# 6 ^ 4 = 2        (third pair 4^4 part cancels: ...^4^4 = 2)
# Result = 2 ✓

def optimal_single_number(arr):
    """Find single number using XOR (OPTIMAL)"""
    xor_result = 0
    
    for num in arr:
        xor_result ^= num
    
    return xor_result

# Test Optimal
l2 = [1, 1, 2, 3, 3, 4, 4]
print("Optimal Result:", optimal_single_number(l2))

# Additional test cases
print("\nAdditional Tests:")
print("Array [0, 0, 1]:", optimal_single_number([0, 0, 1]))  # 1
print("Array [5, 5, 10, 10, 7]:", optimal_single_number([5, 5, 10, 10, 7]))  # 7
print("Array [9]:", optimal_single_number([9]))  # 9





