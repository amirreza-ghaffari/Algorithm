# Time: Nlog(N) + Mlog(M)
# Space: O(1)
def min_distance(array1, array2):
    array1.sort()
    array2.sort()
    min_distance = float('inf')
    idx1 = 0
    idx2 = 0
    while idx1 <= len(array1) - 1 and idx2 <= len(array2) - 1:
        distance = abs(array1[idx1] - array2[idx2])
        if distance < min_distance:
            min_distance = distance
            paris = [array1[idx1], array2[idx2]]

        if array2[idx2] > array1[idx1]:
            idx1 = idx1 + 1
        else:
            idx2 = idx2 + 1
    return paris
