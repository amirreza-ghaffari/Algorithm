def find_max_adjacent_subarray(array):
    current_max = 0
    maximum = -float('inf')
    for value in array:
        current_max = max(current_max + value, value)
        if current_max > maximum:
            maximum = current_max
    return maximum
