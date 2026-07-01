# LeetCode Notes:
# Problem: Every number appears twice except one. Return the single number.
# Idea: XOR all numbers together.
# Trick: Equal values cancel because x ^ x = 0, so only the single value remains.
# Dry run: [1,1,2,3,3,4,4] -> pairs vanish -> answer is 2.
# TC and SC: O(N) time because we scan once, O(1) space because only one XOR variable is used.

def brute_force_single_number(arr):
    """Find single number using hash map (BRUTE FORCE)"""
    freq_map = {}
    
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    for num, freq in freq_map.items():
        if freq == 1:
            return num
    
    return -1

# Test Brute Force
l1 = [1, 1, 2, 3, 3, 4, 4]
print("Brute Force Result:", brute_force_single_number(l1))


def optimal_single_number(arr):
    """Find single number using XOR (OPTIMAL)"""
    xor_result = 0
    
    for num in arr:
        xor_result ^= num
    
    return xor_result

# Test Optimal
l2 = [1, 1, 2, 3, 3, 4, 4]
print("Optimal Result:", optimal_single_number(l2))

print("\nAdditional Tests:")
print("Array [0, 0, 1]:", optimal_single_number([0, 0, 1]))
print("Array [5, 5, 10, 10, 7]:", optimal_single_number([5, 5, 10, 10, 7]))
print("Array [9]:", optimal_single_number([9]))
