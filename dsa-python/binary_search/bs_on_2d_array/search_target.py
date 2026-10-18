# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Eg:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]


def searchTarget(matrix, target) -> bool:
    row_count = len(matrix)
    column_count = len(matrix[0])

    # Binary search to identify the row that may contain the target
    low_row = 0
    high_row = row_count - 1

    while low_row <= high_row:
        middle_row = (low_row + high_row) // 2

        first_value = matrix[middle_row][0]
        last_value = matrix[middle_row][column_count - 1]

        # Target is smaller than the first value,
        # so search the rows above.
        if target < first_value:
            high_row = middle_row - 1

        # Target lies within the range of this row,
        # so perform binary search on this row.
        elif first_value <= target <= last_value:
            low_column = 0
            high_column = column_count - 1

            while low_column <= high_column:
                middle_column = (low_column + high_column) // 2
                middle_value = matrix[middle_row][middle_column]

                if middle_value < target:
                    low_column = middle_column + 1
                elif middle_value > target:
                    high_column = middle_column - 1
                else:
                    return True

            # Target is not present in the only possible row.
            return False

        # Target is greater than the last value,
        # so search the rows below.
        else:
            low_row = middle_row + 1

    return False


print(searchTarget(matrix, 3))

				





 