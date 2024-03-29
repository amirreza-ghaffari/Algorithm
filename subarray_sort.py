#Write a function that takes in an array of integers of length at least 2. The function should return an array of the starting and ending indices of the smallest 
#subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. If the input array is already sorted, the function should return [-1, -1].


# Time: O(N)
# Space: O(1)

def check_in_order(array, i):
    if i == 0:
        return array[0] < array[1]
    elif i == len(array) - 1:
        return array[i] > array[i-1]
    if 0 < i < len(array) and array[i - 1] < array[i] < array[i + 1]:
        return True
    return False


def main(array):
    min_not_sorted = float('inf')
    max_not_sorted = -float('inf')
    for i in range(0, len(array)):
        if not check_in_order(array, i):
            min_not_sorted = min(min_not_sorted, array[i])
            max_not_sorted = max(max_not_sorted, array[i])

    if min_not_sorted == float('inf'):
        return [-1, -1]
    left_idx = 0
    while array[left_idx] <= min_not_sorted:
        left_idx = left_idx + 1

    right_idx = len(array) - 1
    while array[right_idx] >= max_not_sorted:
        right_idx = right_idx - 1

    return [left_idx, right_idx]
