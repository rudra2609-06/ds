'''
╔════════════════════════════════════════════════════════════════════════════════╗
║                    REMOVE DUPLICATES FROM SORTED ARRAY                         ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║ PROBLEM DESCRIPTION:                                                           ║
║ ───────────────────                                                            ║
║ Given a sorted array with duplicate elements, remove duplicates in-place.     ║
║ Each unique element should appear only once. Return the count of unique       ║
║ elements. The rest of the array (after unique elements) doesn't matter.       ║
║                                                                                ║
║ EXAMPLE:                                                                       ║
║ • Input:  [1, 1, 2, 2, 4, 5, 6, 6]                                           ║
║ • Output: Array first 5 elements = [1, 2, 4, 5, 6] (rest can be anything)   ║
║ • Count:  5 unique elements                                                   ║
║                                                                                ║
║ KEY OBSERVATIONS:                                                              ║
║ • Array is SORTED - consecutive duplicates are adjacent                       ║
║ • Must modify in-place without extra space                                    ║
║ • Return count of unique elements                                            ║
║ • Elements after count position don't matter                                 ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
'''

# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE - Mark and Remove (Multiple Passes)
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N²)  - Each duplicate removal requires shifting
# Space Complexity: O(1)   - Only using constant extra space
#
# HOW IT WORKS:
# 1. Iterate through array
# 2. When duplicate found, remove it (shift all elements left)
# 3. Continue until end of array
# 4. Result: duplicates removed, unique elements preserved
#
# PROBLEM WITH THIS APPROACH:
# • Shifting elements is O(N), doing it N times = O(N²)
# • Slow for large arrays
#
# EXAMPLE: [1,1,2,2,4]
# Find duplicate 1 at index 1 → [1,2,2,4]
# Find duplicate 2 at index 1 → [1,2,4]
# Result: [1,2,4] ✓

def brute_force_remove_duplicates(arr):
    """Remove duplicates using brute force (multiple passes with removal)"""
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            # Remove duplicate by shifting all elements left
            arr.pop(i + 1)
        else:
            i += 1
    return len(arr)

# Test Brute Force
l1 = [1, 1, 2, 2, 4, 5, 6, 6]
count = brute_force_remove_duplicates(l1.copy())
print(f"Brute Force - Unique count: {count}")


# ═══════════════════════════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL - Two-Pointer In-Place Modification
# ═══════════════════════════════════════════════════════════════════════════════
# Time Complexity:  O(N)   - Single pass through array
# Space Complexity: O(1)   - In-place modification
#
# HOW IT WORKS:
# 1. Use two pointers: i (write position) and j (read position)
# 2. i tracks where to place next unique element
# 3. j scans through array looking for different elements
# 4. When arr[j] ≠ arr[i], place it at position i+1 and increment i
# 5. Continue until end of array
#
# KEY INSIGHT:
# • First element is always unique, start i at 0
# • Compare arr[j] with arr[i] (last unique we placed)
# • If different, place at i+1 (it's unique)
# • Only modify first (i+1) positions, rest doesn't matter
#
# EXAMPLE: [1,1,2,2,4,5,6,6]
#           i=0
# j scans: arr[1]=1 (same as arr[0]) skip
#          arr[2]=2 (diff from arr[0]) → place at i+1=1 → arr=[1,2,2,2,4,5,6,6], i=1
#          arr[3]=2 (same as arr[1]) skip
#          arr[4]=4 (diff from arr[1]) → place at i+1=2 → arr=[1,2,4,2,4,5,6,6], i=2
#          ... continue ...
# Result: First 5 elements [1,2,4,5,6] are unique ✓

def optimal_remove_duplicates(arr):
    """Remove duplicates using two-pointer technique (OPTIMAL)"""
    if len(arr) == 0:
        return 0
    
    i = 0  # Pointer to place next unique element
    
    # j scans through array
    for j in range(1, len(arr)):
        # If current element is different from last unique element
        if arr[j] != arr[i]:
            # Place it at next position and move i forward
            i += 1
            arr[i] = arr[j]
    
    # Return count of unique elements
    return i + 1

# Test Optimal
l2 = [1, 1, 2, 2, 4, 5, 6, 6]
count = optimal_remove_duplicates(l2)
print(f"Optimal - Unique count: {count}")
print(f"First {count} elements: {l2[:count]}")
