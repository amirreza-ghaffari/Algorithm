# ---------------- First Solution -----------------
# Time: O(1)

def main(array):

    if len(array) == 1:
        return 1

    aux = [0 for i in range(0, len(array))]
    aux[0] = 1
    min_value = float('inf')
    for idx in range(1,len(array)):
        if array[idx] > array[idx - 1]:
            aux[idx] = aux[idx -1] + 1
        else:
            aux[idx] = aux[idx - 1] - 1

        if aux[idx] < min_value:
            min_value = aux[idx]

    if min_value < 1:
        aux = [x + (1-min_value) for x in aux]

    if array[0] < array[1]:
        aux[0] = 1
    if array[-1] < array[-2]:
        aux[-1] = 1

    return sum(aux)
    
 # --------------Second Solution ---------------
 # Time: O(N)
 # Space : O(1)
 
 
def main(array):

    if len(array) == 2:
        return 3
    if len(array) == 1:
        return 1

    rewards = [1 for i in range(0, len(array))]
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            rewards[i] = rewards[i-1] + 1

    for i in reversed(range(len(array)-1)):
        if array[i] > array[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1] + 1)

    return rewards
