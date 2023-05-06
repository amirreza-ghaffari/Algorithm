# Time: O(N)
# Space: O(N)

def sum_two_value(array, target):
    t = {}
    for i in range(0, len(array)):
        if array[i] in t:
            return t[array[i]], i
        else:
            t[target-array[i]] = i
    return False
