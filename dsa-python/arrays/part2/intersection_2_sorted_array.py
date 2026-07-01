# LeetCode Notes:
# Problem: Return the common elements of two sorted arrays.
# Idea: Use two pointers and compare current values.
# Trick: Move the pointer with the smaller value because it cannot match later values in the other array.
# Dry run: [1,1,2,3,4,5] and [2,3,4,4,5,6] -> matches are [2,3,4,5].
# TC and SC: O(M+N) time because both pointers move once, O(min(M,N)) space for the answer.

def brute_force_intersection(arr1, arr2):
    """Find intersection using nested loop (BRUTE FORCE)"""
    intersection = []
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                if not intersection or intersection[-1] != arr1[i]:
                    intersection.append(arr1[i])
                break
    
    return intersection

# Test Brute Force
l1 = [1, 1, 2, 3, 4, 5]
l2 = [2, 3, 4, 4, 5, 6]
print("Brute Force Result:", brute_force_intersection(l1, l2))


def optimal_intersection(arr1, arr2):
    """Find intersection using two-pointer technique (OPTIMAL)"""
    intersection = []
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            intersection.append(arr1[i])
            i += 1
            j += 1
    
    return intersection

# Test Optimal
l3 = [1, 1, 2, 3, 4, 5]
l4 = [2, 3, 4, 4, 5, 6]
print("Optimal Result:", optimal_intersection(l3, l4))
