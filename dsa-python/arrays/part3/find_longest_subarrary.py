# LeetCode Notes:
# Problem: Find the length of the longest subarray whose sum is k.
# Idea: Use prefix sum and remember the first index where each prefix was seen.
# Trick: If prefixSum-k was seen before, the subarray in between has sum k.
# Dry run: [10,5,2,7,1,-10], k=15 -> full array sums to 15, so answer becomes 6.
# TC and SC: O(N) time because each index is processed once, O(N) space because prefix sums go in a map.

# Brute force:
# Try every start and end index and keep a running sum.

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


# Optimal:
# Store the first index of each prefix sum.

def optimal_longest_subarray(arr, k):
    """Find longest subarray with sum=k using prefix sum + hash map (OPTIMAL)"""
    max_length = 0
    prefix_sum = 0
    prefix_map = {0: -1}
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_map.get(prefix_sum - k) is not None:
            length = i - prefix_map[prefix_sum - k]
            max_length = max(max_length, length)
        
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    
    return max_length

# Test Optimal
l2 = [10, 5, 2, 7, 1, -10]
k = 15
print("Optimal Result:", optimal_longest_subarray(l2, k))
