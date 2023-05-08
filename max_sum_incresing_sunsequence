# Time: O(N^2)
# Space: O(N)

def main(array):
    sums = []
    greatest = -float("inf")
    for i in range(0, len(array)):
        sums.append(array[i])
        for j in range(0, i):
            if array[j] < array[i] and sums[j] + array[i] > sums[i]:
                sums[i] = sums[j] + array[i]

        if sums[i] > greatest:
            greatest = sums[i]

    return greatest
