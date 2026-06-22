'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                 INTERSECTION OF TWO SORTED ARRAYS                              ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given two sorted arrays, find all common elements (intersection). Each        ║
║ element in the result must appear as many times as it shows in both arrays.   ║
║ Duplicates in both arrays should be included in result.                       ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  arr1 = [1, 1, 2, 3, 4, 5]                                           ║
║           arr2 = [2, 3, 4, 4, 5, 6]                                           ║
║ • Output: [2, 3, 4, 5] (common elements)                                      ║
║                                                                                ║
║ KEY OBSERVATIONS:                                                              ║
║ • Both arrays are SORTED - allows two-pointer approach                        ║
║ • If arr1[i] < arr2[j], move i forward (search in arr1)                       ║
║ • If arr1[i] > arr2[j], move j forward (search in arr2)                       ║
║ • If equal, add to result and move both forward                              ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Nested Loop
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(M * N)   - For each element in arr1, search in arr2
# Space Complexity: O(min(M,N)) - For storing intersection
#
# HOW IT WORKS:
# 1. For each element in first array
# 2. Search for it in second array
# 3. If found and not already added to result, add it
# 4. Mark as used to avoid duplicates
#
# PROBLEM:
# • Nested loops = quadratic time
# • Slow even with sorted arrays
#
# EXAMPLE: [1,1,2,3,4,5] and [2,3,4,4,5,6]
# Search 1 in arr2 - not found
# Search 1 in arr2 - not found
# Search 2 in arr2 - found → add 2
# Search 3 in arr2 - found → add 3
# Search 4 in arr2 - found → add 4
# Search 5 in arr2 - found → add 5
# Result: [2,3,4,5] ✓

def brute_force_intersection(arr1, arr2):
    """Find intersection using nested loop (BRUTE FORCE)"""
    intersection = []
    
    for i in range(len(arr1)):
        # Search arr1[i] in arr2
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                # Avoid duplicates in result
                if not intersection or intersection[-1] != arr1[i]:
                    intersection.append(arr1[i])
                break
    
    return intersection

# Test Brute Force
l1 = [1, 1, 2, 3, 4, 5]
l2 = [2, 3, 4, 4, 5, 6]
print("Brute Force Result:", brute_force_intersection(l1, l2))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Two-Pointer Technique
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(M + N)   - Single pass through both arrays
# Space Complexity: O(min(M,N)) - For storing intersection
#
# HOW IT WORKS:
# 1. Initialize two pointers i and j at start of arr1 and arr2
# 2. Compare elements at both pointers:
#    - If arr1[i] < arr2[j]: increment i (move forward in arr1)
#    - If arr1[i] > arr2[j]: increment j (move forward in arr2)
#    - If equal: add to result, increment both pointers
# 3. Continue until one array is exhausted
# 4. Automatically handles duplicates correctly (only adds when equal)
#
# WHY IT WORKS WITH SORTED ARRAYS:
# • If arr1[i] is too small, no point checking again (arr1 is sorted)
# • Move forward in smaller value's array
# • Only add when values match
#
# EXAMPLE: [1,1,2,3,4,5] and [2,3,4,4,5,6]
#           i=0                j=0
# 1 < 2: i++ → i=1
# 1 < 2: i++ → i=2
# 2 = 2: add 2, i++, j++ → i=3, j=1
# 3 = 3: add 3, i++, j++ → i=4, j=2
# 4 = 4: add 4, i++, j++ → i=5, j=3
# 5 > 4: j++ → j=4
# 5 = 5: add 5, i++, j++ → i=6, j=5
# i exhausted, stop
# Result: [2,3,4,5] ✓

def optimal_intersection(arr1, arr2):
    """Find intersection using two-pointer technique (OPTIMAL)"""
    intersection = []
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            # arr1[i] is smaller, move forward in arr1
            i += 1
        elif arr1[i] > arr2[j]:
            # arr2[j] is smaller, move forward in arr2
            j += 1
        else:
            # Elements are equal - common element found
            intersection.append(arr1[i])
            i += 1
            j += 1
    
    return intersection

# Test Optimal
l3 = [1, 1, 2, 3, 4, 5]
l4 = [2, 3, 4, 4, 5, 6]
print("Optimal Result:", optimal_intersection(l3, l4))


