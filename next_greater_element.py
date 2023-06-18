# ----- with 3 for loop ------
# Time: O(N)
# Space: O(N)

def main(array):
    _max = max(array)
    out = [0 for x in range(0, len(array))]


    first_greater = array[-1]
    for i in range(0, len(array)):
        if array[i] > first_greater:
            first_greater = array[i]
            break

    out[-1] = first_greater

    for i in reversed(range(0, len(array)-1)):
        if array[i] >= array[i+1]:
            out[i] = out[i+1]
        else:
            out[i] = array[i+1]

    out[array.index(max(array))] = -1
    return out
