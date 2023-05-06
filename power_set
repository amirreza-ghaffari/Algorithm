# Time: O(2^N * N)
# Space: O(2^N * N)

def subset(array):
    subset = [[]]
    for value in array:
        for i in range(len(subset)):
            current_subset = subset[i]
            subset.append(current_subset + [value])
    return subset
