'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                  LONGEST SUBARRAY WITH SUM EQUAL TO K                          ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given an array and a target sum K, find the LENGTH of the longest contiguous  ║
║ subarray whose sum equals K. Return 0 if no subarray exists.                  ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  arr = [10, 5, 2, 7, 1, -10], K = 15                                ║
║ • Output: 4 (subarray [5, 2, 7, 1] has sum=15 and length=4)                  ║
║                                                                                ║
║ WHY HASH MAP:                                                                  ║
║ • Subarray sum = prefix_sum[j] - prefix_sum[i]                               ║
║ • We want: prefix_sum[j] - prefix_sum[i] = K                                 ║
║ • Rearrange: prefix_sum[i] = prefix_sum[j] - K                               ║
║ • So for each position, check if (current_sum - K) exists in hash map        ║
║ • If yes, we found a subarray with sum = K                                   ║
║                                                                                ║
║ KEY OBSERVATIONS:                                                              ║
║ • Array can have negative numbers (important for hash map approach)           ║
║ • We need LENGTH of longest subarray, not the subarray itself                ║
║ • Store FIRST occurrence of each prefix sum (to maximize length)             ║
║ • Initialize with {0: -1} to handle subarrays starting from index 0          ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Nested Loops (Check All Subarrays)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N²)   - All pairs of start and end indices
# Space Complexity: O(1)    - Only tracking max length
#
# HOW IT WORKS:
# 1. For each starting position i
# 2. For each ending position j >= i
# 3. Calculate sum of subarray[i:j+1]
# 4. If sum equals K, update max length
#
# PROBLEM:
# • Recalculating sum for each subarray is wasteful
# • We can maintain running sum to optimize slightly
#
# EXAMPLE: [10, 5, 2, 7, 1, -10], K=15
# i=0: [10]=10, [10,5]=15 ✓ len=2
#      [10,5,2]=17, [10,5,2,7]=24, etc.
# i=1: [5]=5, [5,2]=7, [5,2,7]=14, [5,2,7,1]=15 ✓ len=4
# i=2: [2]=2, [2,7]=9, [2,7,1]=10, [2,7,1,-10]=0
# ... continue
# Max length found = 4 ✓

def brute_force_longest_subarray(arr, k):
    """Find longest subarray with sum=k using brute force (BRUTE FORCE)"""
    max_length = 0
    
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == k:
                max_length = max(max_length, j - i + 1)
    
    return max_length

# Test Brute Force
l1 = [10, 5, 2, 7, 1, -10]
k = 15
print("Brute Force Result:", brute_force_longest_subarray(l1, k))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Prefix Sum + Hash Map
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(N)   - Hash map stores prefix sums
#
# HOW IT WORKS:
# 1. Initialize hash map with {0: -1} (handles subarrays from start)
# 2. Maintain prefix_sum as we iterate through array
# 3. For each index, check if (prefix_sum - k) exists in map:
#    - If yes: length = current_index - previous_index (found subarray with sum=k)
#    - Update max_length
# 4. Only store FIRST occurrence of each prefix_sum (to maximize length)
#
# WHY PREFIX SUM WORKS:
# • prefix_sum[j] = sum of arr[0:j+1]
# • prefix_sum[i] = sum of arr[0:i+1]
# • subarray_sum[i+1:j+1] = prefix_sum[j] - prefix_sum[i]
# • If subarray_sum = k, then: prefix_sum[j] - prefix_sum[i] = k
# • Rearrange: prefix_sum[i] = prefix_sum[j] - k
# • So we look for (prefix_sum - k) in our map!
#
# WHY FIRST OCCURRENCE:
# • If we see prefix_sum again, we DON'T update it
# • This way, (j - stored_i) is maximized (longest length)
#
# EXAMPLE: [10, 5, 2, 7, 1, -10], K=15
# map = {0: -1}
# i=0: prefix_sum=10, look for 10-15=-5 in map? No. map[10]=0
# i=1: prefix_sum=15, look for 15-15=0 in map? Yes! At index -1.
#      length = 1 - (-1) = 2. max_length=2. map already has {0: -1}
# i=2: prefix_sum=17, look for 17-15=2 in map? No. map[17]=2
# i=3: prefix_sum=24, look for 24-15=9 in map? No. map[24]=3
# i=4: prefix_sum=25, look for 25-15=10 in map? Yes! At index 0.
#      length = 4 - 0 = 4. max_length=4. Don't update map
# i=5: prefix_sum=15, look for 15-15=0 in map? Yes! At index -1.
#      length = 5 - (-1) = 6. But wait, let's check...
#      Subarray from index 0 to 5: [10,5,2,7,1,-10] = 15 ✓ length=6!
# Result: max_length = 6

def optimal_longest_subarray(arr, k):
    """Find longest subarray with sum=k using prefix sum + hash map (OPTIMAL)"""
    max_length = 0
    prefix_sum = 0
    prefix_map = {0: -1}  # Initialize with {0: -1} to handle from start
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        # Check if (prefix_sum - k) exists in map
        if prefix_map.get(prefix_sum - k) is not None:
            # Found a subarray with sum = k
            length = i - prefix_map[prefix_sum - k]
            max_length = max(max_length, length)
        
        # Store first occurrence of this prefix_sum
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    
    return max_length

# Test Optimal
l2 = [10, 5, 2, 7, 1, -10]
k = 15
print("Optimal Result:", optimal_longest_subarray(l2, k))


		


	



