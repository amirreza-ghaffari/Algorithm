# Space: O(N)
# Time: O(1)
def main(array):
    start_row = 0
    end_row = len(array) - 1

    start_col = 0
    end_col = len(array[0]) - 1

    result = []

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col):
            result.append(array[start_row][col])

        for row in range(start_row, end_row + 1):
            result.append(array[row][end_col])

        for col in reversed(range(start_col, end_col)):
            result.append(array[end_row][col])

        for row in reversed(range(start_row + 1, end_row)):
            result.append(array[row][start_col])

        start_row = start_row + 1
        end_row = end_row - 1
        start_col = start_col + 1
        end_col = end_col - 1
    return array
