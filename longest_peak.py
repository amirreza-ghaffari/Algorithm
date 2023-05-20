# Time: O(N)
# Space: O(1)

def check_length(array, i):
    length = 1
    for j in range(i + 1, len(array)):
        # print(array[j], j)
        if array[j] < array[j-1]:
            # print('yes')
            length = length + 1
        else:
            break

    for j in reversed(range(i + 1)):
        # print(array[j], j)

        if array[j] > array[j-1]:
            length = length + 1
            # print('yes')
        else:
            break

    # print(length)
    return length


def main(array):
    peaks = []
    longest = -float('inf')
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] > array[i + 1]:
            peaks.append(i)
            lengths = check_length(array, i)
            if lengths > longest:
                longest = lengths

    return longest
