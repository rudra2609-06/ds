# LeetCode Notes:
# Problem: Return all unique elements from two sorted arrays in sorted order.
# Idea: Merge both arrays with two pointers and skip duplicates while adding.
# Trick: Before adding, compare with the last inserted value.
# Dry run: [1,1,2,3,4,5] and [2,3,4,4,5,6] -> merged unique answer is [1,2,3,4,5,6].
# TC and SC: O(M+N) time because both pointers move once, O(M+N) space for the result.

def brute_force_union(arr1, arr2):
    """Find union using combine and remove duplicates (BRUTE FORCE)"""
    combined = arr1 + arr2
    combined.sort()
    
    union = []
    for i in range(len(combined)):
        if i == 0 or combined[i] != combined[i - 1]:
            union.append(combined[i])
    
    return union

# Test Brute Force
l1 = [1, 1, 2, 3, 4, 5]
l2 = [2, 3, 4, 4, 5, 6]
print("Brute Force Result:", brute_force_union(l1, l2))


def optimal_union(arr1, arr2):
    """Find union using two-pointer merge (OPTIMAL)"""
    union = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    
    return union

# Test Optimal
l3 = [1, 1, 2, 3, 4, 5]
l4 = [2, 3, 4, 4, 5, 6]
print("Optimal Result:", optimal_union(l3, l4))
