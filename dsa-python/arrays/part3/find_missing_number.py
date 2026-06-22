'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                    FIND MISSING NUMBER IN ARRAY                               ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given an array containing N-1 distinct numbers from the range 1 to N,         ║
║ find the one missing number. Array is unsorted and can be in any order.       ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  arr = [1, 2, 4, 5], N = 5                                           ║
║ • Output: 3 (missing from sequence 1-5)                                       ║
║                                                                                ║
║ APPROACHES COMPARISON:                                                         ║
║ ┌─────────────────┬──────────┬──────────┬────────────────────────────┐        ║
║ │ Approach        │ Time     │ Space    │ Pros/Cons                  │        ║
║ ├─────────────────┼──────────┼──────────┼────────────────────────────┤        ║
║ │ Brute Force     │ O(N²)    │ O(1)     │ Simple but slow            │        ║
║ │ Hash Map        │ O(N)     │ O(N)     │ Fast, uses extra space     │        ║
║ │ Math (Sum)      │ O(N)     │ O(1)     │ Fast, best if no overflow │        ║
║ │ XOR             │ O(N)     │ O(1)     │ Fast, clever, no overflow │        ║
║ └─────────────────┴──────────┴──────────┴────────────────────────────┘        ║
║                                                                                ║
║ BEST CHOICE: XOR Approach (Magic!)                                            ║
║ • Same complexity as Math but works with very large numbers                   ║
║ • XOR Property: a ^ a = 0, a ^ 0 = a, XOR is commutative & associative      ║
║ • XOR all numbers from 1 to N and all numbers in array                       ║
║ • Duplicate numbers cancel out (XOR with themselves = 0)                      ║
║ • Result is the missing number                                               ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Search for Each Number
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N²)   - For each number 1 to N, search in array
# Space Complexity: O(1)    - No extra space
#
# HOW IT WORKS:
# 1. For each number from 1 to N
# 2. Search for it in the array
# 3. If not found, it's the missing number
#
# PROBLEM:
# • Very slow! O(N²) is terrible for large N
#
# EXAMPLE: [1, 2, 4, 5], N=5
# Search 1 - found
# Search 2 - found
# Search 3 - NOT found ✓ (missing number = 3)

def brute_force_find_missing(arr):
    """Find missing number by searching for each number (BRUTE FORCE)"""
    n = len(arr) + 1  # Since one number is missing
    
    for num in range(1, n + 1):
        if num not in arr:
            return num
    
    return -1

# Test Brute Force
l1 = [1, 2, 4, 5]
print("Brute Force Result:", brute_force_find_missing(l1))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Math Approach (Sum Formula)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(1)   - Only two variables
#
# HOW IT WORKS:
# 1. Calculate expected sum using formula: N*(N+1)/2 (sum of 1 to N)
# 2. Calculate actual sum of array elements
# 3. Missing = Expected - Actual
#
# WHY IT WORKS:
# • Sum of 1 to N = N*(N+1)/2 (mathematical formula)
# • If we remove one number, actual_sum < expected_sum
# • The difference is the missing number
#
# DRAWBACK:
# • Can overflow with very large numbers (in some languages)
# • Python handles big integers, so not an issue here
#
# EXAMPLE: [1, 2, 4, 5], N=5
# Expected sum = 5 * 6 / 2 = 15
# Actual sum = 1 + 2 + 4 + 5 = 12
# Missing = 15 - 12 = 3 ✓

def math_find_missing(arr):
    """Find missing number using sum formula (OPTIMAL - Math)"""
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Test Math Approach
l2 = [1, 2, 4, 5]
print("Math Result:", math_find_missing(l2))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 3: MOST OPTIMAL - XOR Approach (The Magic)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(1)   - Only two variables
#
# HOW IT WORKS:
# 1. XOR all numbers from 1 to N: xor1 = 1 ^ 2 ^ 3 ^ ... ^ N
# 2. XOR all numbers in array:   xor2 = arr[0] ^ arr[1] ^ ... ^ arr[N-2]
# 3. Result: xor1 ^ xor2 = missing number
#
# WHY XOR WORKS (The Magic):
# • XOR Property 1: a ^ a = 0 (any number XOR itself = 0)
# • XOR Property 2: a ^ 0 = a (any number XOR 0 = itself)
# • XOR Property 3: XOR is commutative & associative
#
# • When we XOR all numbers 1 to N and all array elements:
#   - Each number in array appears once in both lists
#   - (num ^ num) = 0 for all numbers in array
#   - All numbers cancel out to 0
#   - Only missing number doesn't have a pair
#   - Result: 0 ^ 0 ^ ... ^ missing_number = missing_number
#
# ADVANTAGES:
# • No overflow issues (XOR doesn't grow like sum)
# • Elegant and clever solution
# • Same O(N) time as Math approach but more robust
#
# EXAMPLE: [1, 2, 4, 5], N=5
# xor1 = 1 ^ 2 ^ 3 ^ 4 ^ 5 = 1 (binary: 001)
# xor2 = 1 ^ 2 ^ 4 ^ 5 = 6 (binary: 110)
# result = 1 ^ 6 = 7 Wait, that's wrong. Let me recalculate...
# 
# Actually let me verify:
# 1 = 001
# 2 = 010
# 3 = 011
# 4 = 100
# 5 = 101
# 
# xor1 = 001 ^ 010 ^ 011 ^ 100 ^ 101
#      = 011 ^ 011 ^ 100 ^ 101  (001 ^ 010 = 011)
#      = 000 ^ 100 ^ 101        (011 ^ 011 = 000)
#      = 100 ^ 101              (000 ^ 100 = 100)
#      = 001                    (100 ^ 101 = 001) ✓
#
# xor2 = 001 ^ 010 ^ 100 ^ 101
#      = 011 ^ 100 ^ 101        (001 ^ 010 = 011)
#      = 111 ^ 101              (011 ^ 100 = 111)
#      = 010                    (111 ^ 101 = 010) ✓
#
# result = 001 ^ 010 = 011 = 3 ✓

def xor_find_missing(arr):
    """Find missing number using XOR (MOST OPTIMAL)"""
    n = len(arr) + 1
    xor1 = 0  # XOR of all numbers 1 to N
    xor2 = 0  # XOR of all array elements
    
    # XOR all numbers from 1 to N
    for i in range(1, n + 1):
        xor1 ^= i
    
    # XOR all array elements
    for num in arr:
        xor2 ^= num
    
    # XOR of both results gives missing number
    return xor1 ^ xor2

# Test XOR Approach
l3 = [1, 2, 4, 5]
print("XOR Result:", xor_find_missing(l3))

# Additional test case
print("\nAdditional Tests:")
print("Array [3, 4, 1]:", xor_find_missing([3, 4, 1]))  # Missing 2
print("Array [1]:", xor_find_missing([1]))  # Missing 2
print("Array [2]:", xor_find_missing([2]))  # Missing 1