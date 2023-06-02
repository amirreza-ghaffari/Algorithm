# Time: O(N)
# Space: O(N)


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



def node_search(i, j, array, mask):
    nodes_to_explore = [[i, j]]
    is_edge = False
    l = []
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if mask[i][j]:
            continue
        mask[i][j] = True
        if array[i][j] == 0:
            continue
        l.append([i, j])
        if i == 0 or i == len(array) -1 or j == 0 or j == len(array[0]) - 1:
            is_edge = True
        for h in get_neighbours(i, j, array, mask):
            nodes_to_explore.append(h)
    return l, is_edge


def main(array):
    mask = [[False for column in row] for row in array]
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if mask[i][j]:
                continue
            l, is_edge = node_search(i, j, array, mask)
            if is_edge is False:
                for item in l:
                    array[item[0]][item[1]] = 0
    return array
