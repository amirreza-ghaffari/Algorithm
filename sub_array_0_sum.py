# Time: O(N)
# Space: O(N)
def main(array):
    all_sums = {array[0]: 0}
    _sum = array[0]
    for i in range(1, len(array)):
        _sum = _sum + array[i]
        if _sum == 0:
            return array[:i+1]
        elif _sum in all_sums:
            return array[all_sums[_sum]+1:i+1]
        else:
            all_sums[_sum] = i
    return False
