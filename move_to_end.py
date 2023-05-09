# Time: O(n)
# Space: O(1)

def move_to_end(array, target):
    lef_idx = 0
    right_idx = len(array) - 1
    while lef_idx < right_idx:

        if array[right_idx] == target:
            right_idx = right_idx - 1
        if array[lef_idx] == target:
            temp = array[right_idx]
            array[lef_idx] = temp
            array[right_idx] = target
        lef_idx = lef_idx + 1
    return array
