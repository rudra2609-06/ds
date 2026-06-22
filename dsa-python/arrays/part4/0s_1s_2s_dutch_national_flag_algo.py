'''
╔════════════════════════════════════════════════════════════════════════════════╗
║        SORT ARRAY OF 0s, 1s AND 2s (Dutch National Flag Algorithm)            ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given an array containing only 0s, 1s, and 2s, sort it in-place without      ║
║ using any sorting algorithm. All 0s should come first, then 1s, then 2s.     ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  arr = [1, 2, 1, 0, 2, 0, 1]                                        ║
║ • Output: [0, 0, 1, 1, 1, 2, 2]                                              ║
║                                                                                ║
║ KEY CONSTRAINTS:                                                               ║
║ • Only contains 0s, 1s, and 2s (limited values)                               ║
║ • Must sort in-place (O(1) space)                                             ║
║ • Must do it in ONE pass or minimal passes                                    ║
║ • No standard sorting algorithm                                               ║
║                                                                                ║
║ WHY DUTCH NATIONAL FLAG:                                                       ║
║ • Named after Dutch flag (3 colored stripes)                                  ║
║ • 3 colors/values → 3-way partitioning problem                                ║
║ • Uses 3 pointers to partition array into 3 regions:                         ║
║   - Left (0s), Middle (1s), Right (2s)                                       ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Count and Overwrite
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Multiple passes (but still linear)
# Space Complexity: O(1)   - Only extra variables, no extra array
#
# HOW IT WORKS:
# 1. Count number of 0s, 1s, and 2s in array
# 2. Overwrite array: first count_0s elements = 0, next count_1s elements = 1, rest = 2
#
# ADVANTAGE:
# • Simple to understand
# • Single pass for counting, one pass for writing
#
# DISADVANTAGE:
# • Not as elegant as three-pointer approach
# • Loses original values during overwriting
#
# EXAMPLE: [1, 2, 1, 0, 2, 0, 1]
# Count: 0s=2, 1s=3, 2s=2
# Overwrite positions:
#   0-1: write 0 → [0, 0, 1, 0, 2, 0, 1]
#   2-4: write 1 → [0, 0, 1, 1, 1, 0, 1]
#   5-6: write 2 → [0, 0, 1, 1, 1, 2, 2]

def brute_force_sort_012(arr):
    """Sort 0s, 1s, 2s by counting (BRUTE FORCE)"""
    count_0 = 0
    count_1 = 0
    count_2 = 0
    
    # Count occurrences
    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1
    
    # Overwrite array
    idx = 0
    
    # Write all 0s
    for _ in range(count_0):
        arr[idx] = 0
        idx += 1
    
    # Write all 1s
    for _ in range(count_1):
        arr[idx] = 1
        idx += 1
    
    # Write all 2s
    for _ in range(count_2):
        arr[idx] = 2
        idx += 1
    
    return arr

# Test Brute Force
l1 = [1, 2, 1, 0, 2, 0, 1]
print("Brute Force Result:", brute_force_sort_012(l1.copy()))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Dutch National Flag (Three-Pointer)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(1)   - In-place, no extra space
#
# HOW IT WORKS:
# Use THREE pointers to maintain three regions:
# • LOW (left):    marks boundary where 0s should be
# • MID (middle):  current element being examined
# • HIGH (right):  marks boundary where 2s should be
#
# REGIONS AT ANY TIME:
# [0...low-1] = all 0s (final)
# [low...mid-1] = all 1s (being built)
# [mid...high] = unknown (being examined)
# [high+1...n-1] = all 2s (final)
#
# LOGIC:
# • If arr[mid] == 0: swap with arr[low], move both forward
# • If arr[mid] == 1: just move mid forward
# • If arr[mid] == 2: swap with arr[high], move high backward (don't advance mid!)
#
# WHY NOT ADVANCE MID FOR 2?
# • After swap from high, new arr[mid] is unknown
# • Might be 0, 1, or 2 - need to check again
# • So don't advance mid yet
#
# EXAMPLE: [1, 2, 1, 0, 2, 0, 1]
#           L  M              H
# Initial state:
# [1, 2, 1, 0, 2, 0, 1]
#  L  M              H
#
# mid=0, arr[0]=1: Just move mid → mid=1
# [1, 2, 1, 0, 2, 0, 1]
#  L     M           H
#
# mid=1, arr[1]=2: Swap with high → swap(arr[1], arr[6])
# [1, 1, 2, 0, 2, 0, 2]
#  L     M        H
# Don't advance mid, move high backward → H=5
# [1, 1, 2, 0, 2, 0, 2]
#  L     M     H
#
# mid=1, arr[1]=1: Just move mid → mid=2
# [1, 1, 2, 0, 2, 0, 2]
#  L        M     H
#
# mid=2, arr[2]=2: Swap with high → swap(arr[2], arr[5])
# [1, 1, 0, 0, 2, 2, 2]
#  L        M  H
# Move high backward → H=4
# [1, 1, 0, 0, 2, 2, 2]
#  L        M  H
#
# mid=2, arr[2]=0: Swap with low → swap(arr[2], arr[1])
# Wait, that's wrong. When mid==low, we're at the same spot.
# Let me restart more carefully...
#
# Actually let me trace through the optimal algorithm implementation:
# mid <= high is the condition, not mid < high
# 
# [1, 2, 1, 0, 2, 0, 1]
#  0  1  2  3  4  5  6
# low=0, mid=0, high=6
#
# Iteration 1: arr[mid]=arr[0]=1, do nothing, mid++ → mid=1
# [1, 2, 1, 0, 2, 0, 1], low=0, mid=1, high=6
#
# Iteration 2: arr[mid]=arr[1]=2, swap(arr[1],arr[6]), high-- → 
# [1, 1, 2, 0, 2, 0, 2], low=0, mid=1, high=5
#
# Iteration 3: arr[mid]=arr[1]=1, do nothing, mid++ → mid=2
# [1, 1, 2, 0, 2, 0, 2], low=0, mid=2, high=5
#
# Iteration 4: arr[mid]=arr[2]=2, swap(arr[2],arr[5]), high-- →
# [1, 1, 0, 0, 2, 2, 2], low=0, mid=2, high=4
#
# Iteration 5: arr[mid]=arr[2]=0, swap(arr[2],arr[0]), low++, mid++ →
# [0, 1, 1, 0, 2, 2, 2], low=1, mid=3, high=4
#
# Iteration 6: arr[mid]=arr[3]=0, swap(arr[3],arr[1]), low++, mid++ →
# [0, 0, 1, 1, 2, 2, 2], low=2, mid=4, high=4
#
# Iteration 7: mid=4, high=4, so mid <= high is true
# arr[mid]=arr[4]=2, swap(arr[4],arr[4]) (swap with self), high-- →
# [0, 0, 1, 1, 2, 2, 2], low=2, mid=4, high=3
#
# Now mid > high, so stop
# Final: [0, 0, 1, 1, 2, 2, 2] ✓ Perfect!

def optimal_sort_012(arr):
    """Sort 0s, 1s, 2s using Dutch National Flag (OPTIMAL)"""
    low = 0      # Boundary for 0s
    mid = 0      # Current examining element
    high = len(arr) - 1  # Boundary for 2s
    
    while mid <= high:
        if arr[mid] == 0:
            # Swap with low region and advance both
            #low to mid-1 → guaranteed all 1s (already explored)
            # So when arr[mid] == 0, swap with low → you know a 1 comes to mid
            # No surprise → safely increment both low and mid
            # arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # Already in correct region, just advance
            mid += 1
        else:  # arr[mid] == 2
            # Swap with high region, retreat high (don't advance mid)
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # Note: mid is NOT incremented because we need to check
            # the swapped element that's now at arr[mid]
    
    return arr

# Test Optimal
l2 = [1, 2, 1, 0, 2, 0, 1]
print("Optimal Result:", optimal_sort_012(l2))

# Additional test cases
print("\nAdditional Tests:")
print("Array [0, 1, 2]:", optimal_sort_012([0, 1, 2]))  # Already sorted
print("Array [2, 1, 0]:", optimal_sort_012([2, 1, 0]))  # Reverse
print("Array [2, 2, 2, 0, 0, 1]:", optimal_sort_012([2, 2, 2, 0, 0, 1]))  # Grouped
		

