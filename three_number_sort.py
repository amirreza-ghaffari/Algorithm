# --------- First Solution -----------
# ----------with 2 for loops --------
# Time: O(N)
# Space: O(1)
def main(array, order):
    left_idx = 0
    right_idx = len(array) - 1

    for i in range(0, len(array)):
        if array[i] == order[0]:
            array[i] = array[left_idx]
            array[left_idx] = order[0]
            left_idx = left_idx + 1

    for i in reversed(range(len(array))):
        if array[i] == order[-1]:
            array[i] = array[right_idx]
            array[right_idx] = order[-1]
            right_idx = right_idx - 1

    return array
# --------- Second Solution -----------
# ----------with 1 for loops --------
# Time: O(N)
# Space: O(1)
def main2(array, order):
    first_idx = 0
    second_idx = 0
    third_idx = len(array) -1


    while second_idx< third_idx:
        if array[second_idx] == order[1]:
            second_idx = second_idx + 1
            continue
        if array[second_idx] == order[0]:
            array[second_idx] = array[first_idx]
            array[first_idx] = order[0]
            first_idx = first_idx + 1
            second_idx = second_idx + 1
            continue

        if array[second_idx] == order[-1]:
            array[second_idx] = array[third_idx]
            array[third_idx] = order[-1]
            third_idx = third_idx - 1
    return array
