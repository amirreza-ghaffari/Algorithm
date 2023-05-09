# Time: O(N^2)
# Space: O(N)
def find_triplets(array, target):
    triplets = []
    array.sort()
    for i in range(0, len(array)):
        right_idx = len(array) - 1
        left_idx = 1 + i
        constant = array[i]
        while left_idx < right_idx:
            sum_ = constant + array[left_idx] + array[right_idx]
            if sum_ == target:
                triplets.append([constant, array[left_idx], array[right_idx]])
                left_idx = left_idx + 1
                right_idx = right_idx - 1
            elif sum_ > target:
                right_idx = right_idx - 1
            else:
                left_idx = left_idx + 1
    return triplets


# quick sort takes Nlog(N) time complexitiy but it is lower than two for loop over a array (O(N^2)). So the time complexity is O(N^2)
