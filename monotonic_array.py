# Time: O(n)
# Space: O(1)

def check_monotonic(array):
    if len(array) == 2:
        return True
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        print(direction)

        new_direction = array[i] - array[i-1]
        if new_direction * direction < 0:
            return False
        if new_direction == 0 :
            continue
        direction = new_direction

    return True
