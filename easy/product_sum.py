# Time: O(N)
# Space: O(1)

# recursive version


def find_sum(arr, m, _sum):

    for idx, item in enumerate(arr):

        if isinstance(item, int):
            _sum = _sum + item
        else:
            _sum = _sum + find_sum(item, m+1, 0)
    return _sum * m
