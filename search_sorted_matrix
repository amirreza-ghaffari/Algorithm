# Time: O(N + M)
# Space: O(1)

def find_value(array, target):
    row_idx = 0
    col_idx = len(array[0]) - 1
    while row_idx <= len(array) - 1 and col_idx <= len(array[0]) - 1:
        potential = array[row_idx][col_idx]
        if potential == target:
            return [row_idx, col_idx]
        if potential > target:
            col_idx = col_idx - 1
        else:
            row_idx = row_idx + 1
