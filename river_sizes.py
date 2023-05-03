# Time: O(n)
# Space: O(n)

def main(array):
    river_sizes = []
    mask = [[False for column in row] for row in array]
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if mask[i][j]:
                continue
            node_search(i, j, array, mask, river_sizes)
    return river_sizes


def node_search(i, j, array, mask, river_sizes):
    river_length = 0
    nodes_to_explore = [[i, j]]
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if mask[i][j]:
            continue
        mask[i][j] = True
        if array[i][j] == 0:
            continue
        river_length = river_length + 1
        for neighbour in get_neighbours(i, j, array, mask):
            nodes_to_explore.append(neighbour)
    if river_length > 0:
        river_sizes.append(river_length)


def get_neighbours(i, j, array, mask):
    neighbours = []
    if i > 0 and not mask[i-1][j]:
        neighbours.append([i-1, j])
    if i < len(array) - 1 and not mask[i+1][j]:
        neighbours.append([i+1, j])

    if j > 0 and not mask[i][j-1]:
        neighbours.append([i, j-1])
    if j < len(array[i]) - 1 and not mask[i][j+1]:
        neighbours.append([i, j+1])
    return neighbours
