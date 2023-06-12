# Time: O(N)
# Space: O(N)

def main(array, direction):
    max_height = -float('inf')
    out = []
    if direction == 'WEST':
        for i in range(0, len(array)):
            if array[i] > max_height:
                out.append(i)
                max_height = array[i]

    else:
        for i in reversed(range(0, len(array))):
            if array[i] > max_height:
                out.append(i)
                max_height = array[i]

    return out
