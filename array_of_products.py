# Space: O(N)
# Time: O(N)

def main(array):
    left_arr = [1 for i in range(0, len(array))]
    right_arr = [1 for i in range(0, len(array))]

    product = 1

    for i in range(0, len(array)):
        left_arr[i] = product
        product = product * array[i]

    product = 1

    for i in reversed(range(len(array))):
        right_arr[i] = product
        product = product * array[i]

    product_arr = [i*j for i, j in zip(left_arr, right_arr)]
    return product_arr
