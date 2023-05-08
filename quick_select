def quick_select(array, k):
    position = k-1
    return quick_select_helper(array ,0, len(array)-1, position)



def quick_select_helper(array, start_idx, end_idx, position):

    while True:
        if start_idx > end_idx:
            raise Exception("something went wrong")

        pivot_idx = start_idx
        left_idx = start_idx + 1
        right_idx = end_idx
        while left_idx <=right_idx:
            if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
                swap(left_idx, right_idx, array)
            if array[left_idx] <= array[pivot_idx]:
                left_idx = left_idx + 1
            if array[right_idx] >= array[pivot_idx]:
                right_idx = right_idx - 1
        swap(pivot_idx, right_idx, array)
        if right_idx == position:
            return array[right_idx]
        elif right_idx < position:
            start_idx = right_idx + 1
        else:
            end_idx = right_idx - 1
         







def swap(one, two ,array):
    array[one], array[two] = array[two], array[one]
