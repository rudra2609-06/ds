'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                    UNION OF TWO SORTED ARRAYS                                  ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given two sorted arrays, find all unique elements from both arrays combined.  ║
║ Return all distinct elements in sorted order. Duplicates should appear once.  ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  arr1 = [1, 1, 2, 3, 4, 5]                                           ║
║           arr2 = [2, 3, 4, 4, 5, 6]                                           ║
║ • Output: [1, 2, 3, 4, 5, 6] (all unique from both, sorted)                  ║
║                                                                                ║
║ KEY OBSERVATIONS:                                                              ║
║ • Both arrays are SORTED - allows two-pointer merge                           ║
║ • Must avoid duplicates in result                                            ║
║ • After one array exhausted, add remaining from other                        ║
║ • Result size = O(M + N) in worst case (no common elements)                  ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Combine and Remove Duplicates
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O((M+N) log (M+N)) - Sorting dominates
# Space Complexity: O(M + N)            - For combined array
#
# HOW IT WORKS:
# 1. Combine both arrays
# 2. Sort combined array
# 3. Iterate through sorted array and add only unique elements
#
# DISADVANTAGE:
# • We already have sorted arrays but we're sorting again!
# • Wastes the sorted property
#
# EXAMPLE: [1,1,2,3,4,5] and [2,3,4,4,5,6]
# Combined: [1,1,2,3,4,5,2,3,4,4,5,6]
# Sorted:   [1,1,2,2,3,3,4,4,4,5,5,6]
# Unique:   [1,2,3,4,5,6] ✓

def brute_force_union(arr1, arr2):
    """Find union using combine and remove duplicates (BRUTE FORCE)"""
    # Combine both arrays
    combined = arr1 + arr2
    
    # Sort the combined array
    combined.sort()
    
    # Extract unique elements
    union = []
    for i in range(len(combined)):
        # Add if first element or different from previous
        if i == 0 or combined[i] != combined[i - 1]:
            union.append(combined[i])
    
    return union

# Test Brute Force
l1 = [1, 1, 2, 3, 4, 5]
l2 = [2, 3, 4, 4, 5, 6]
print("Brute Force Result:", brute_force_union(l1, l2))


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Two-Pointer Merge (Takes Advantage of Sorted Arrays)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(M + N)   - Single pass through both arrays
# Space Complexity: O(M + N)   - For storing union elements
#
# HOW IT WORKS:
# 1. Initialize two pointers i and j at start of arr1 and arr2
# 2. Compare elements at both pointers:
#    - If arr1[i] <= arr2[j]: add arr1[i] if not already added, increment i
#    - Else: add arr2[j] if not already added, increment j
# 3. When one array exhausted, add remaining from other array
# 4. Skip duplicates by checking against last added element
#
# WHY IT WORKS WITH SORTED ARRAYS:
# • No need to re-sort! Already sorted.
# • Merge using two pointers (like merge in merge sort)
# • Naturally handles duplicates by comparing with previous element
#
# EXAMPLE: [1,1,2,3,4,5] and [2,3,4,4,5,6]
#           i=0              j=0
# 1 <= 2: add 1, i++ → [1]
# 1 <= 2: skip (duplicate), i++ → [1]
# 2 <= 2: add 2, i++, j++ → [1,2]
# 3 <= 3: add 3, i++, j++ → [1,2,3]
# 4 <= 4: add 4, i++, j++ → [1,2,3,4]
# 5 <= 4: (5 > 4) add 4, j++ → [1,2,3,4,4]
#   wait, that's wrong. Let me reconsider...
#
# Actually better approach: At each step, pick the smaller (or equal) element
# 1 <= 2: add 1, i++ → result=[1]
# 1 <= 2: add 1? No, already added 1. i++ → result=[1]
# 2 = 2: add 2, i++, j++ → result=[1,2]
# 3 = 3: add 3, i++, j++ → result=[1,2,3]
# 4 = 4: add 4, i++, j++ → result=[1,2,3,4]
# 5 > 4: add 4? No, 4 already in result. j++ → result=[1,2,3,4]
# 5 = 5: add 5, i++, j++ → result=[1,2,3,4,5]
# i exhausted, add remaining from arr2: 6 → result=[1,2,3,4,5,6]

def optimal_union(arr1, arr2):
    """Find union using two-pointer merge (OPTIMAL)"""
    union = []
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    
    # Merge both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            # Take from arr1 if smaller or equal
            # Add only if not already added (check previous element)
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            # Take from arr2 if smaller
            # Add only if not already added
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1
    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    
    # Add remaining elements from arr2
    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    
    return union

# Test Optimal
l3 = [1, 1, 2, 3, 4, 5]
l4 = [2, 3, 4, 4, 5, 6]
print("Optimal Result:", optimal_union(l3, l4))



