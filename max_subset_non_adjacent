# Time: O(N)
# Space: O(N)

def max_sum_non_adjacent(array):
    max_value = -float('inf')
    max_sums = [array[0]]
    max_sums.append(max(array[0], array[1]))

    for i in range(2, len(array)):
        value = max(max_sums[i-1], max_sums[i-2] + array[i])
        max_sums.append(value)
        if value > max_value:
            max_value = value
    return max_value
