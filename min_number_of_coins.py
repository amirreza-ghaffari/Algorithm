# Time: O(n * target)
# Space: O(target)

def main(array, target):
    aux = [float('inf') for i in range(0, target + 1)]
    aux[0] = 0
    for i in range(0, len(array)):
        for j in range(0, len(aux)):
            if j >= array[i]:
                aux[j] = min(aux[j], 1 + aux[j- array[i]])

    return aux[-1]
