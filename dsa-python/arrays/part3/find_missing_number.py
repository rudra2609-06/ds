# LeetCode Notes:
# Problem: Numbers from 1 to N are given with one missing. Find that missing number.
# Idea: XOR values from 1 to N and XOR all array values.
# Trick: Same numbers cancel in XOR, so the missing one is left.
# Dry run: [1,2,4,5], N=5 -> (1^2^3^4^5) ^ (1^2^4^5) = 3.
# TC and SC: O(N) time because we do linear passes, O(1) space because only XOR variables are used.

# Brute force:
# Check every number from 1 to N and return the one not present.

def brute_force_find_missing(arr):
    """Find missing number by searching for each number (BRUTE FORCE)"""
    n = len(arr) + 1
    
    for num in range(1, n + 1):
        if num not in arr:
            return num
    
    return -1

# Test Brute Force
l1 = [1, 2, 4, 5]
print("Brute Force Result:", brute_force_find_missing(l1))


# Better:
# Missing number = expected sum - actual sum.

def math_find_missing(arr):
    """Find missing number using sum formula (OPTIMAL - Math)"""
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Test Math Approach
l2 = [1, 2, 4, 5]
print("Math Result:", math_find_missing(l2))


# Optimal:
# XOR 1..N and all array values.

def xor_find_missing(arr):
    """Find missing number using XOR (MOST OPTIMAL)"""
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0
    
    for i in range(1, n + 1):
        xor1 ^= i
    
    for num in arr:
        xor2 ^= num
    
    return xor1 ^ xor2

# Test XOR Approach
l3 = [1, 2, 4, 5]
print("XOR Result:", xor_find_missing(l3))

print("\nAdditional Tests:")
print("Array [3, 4, 1]:", xor_find_missing([3, 4, 1]))
print("Array [1]:", xor_find_missing([1]))
print("Array [2]:", xor_find_missing([2]))
