# ------------------- First solution----------
# Time: O(N^2)
# Space: O(1)

def main(array):
    current_idx = 0
    total_jumps = 0
    while current_idx < len(array):
        print(current_idx)
        if a[current_idx] + current_idx >= len(array) - 1:
            total_jumps = total_jumps + 1
            return total_jumps
        else:
            total_jumps = total_jumps + 1
            current_idx = find_best_jump(array, current_idx)
    return total_jumps



def find_best_jump(array, i):
    max_value = -float('inf')
    max_index = None
    for j in range(i + 1, array[i] + i + 1):
        if array[j] >= max_value:
            max_value = array[j]
            max_index = j
    return max_index
    
 
 
 # --------------Second Solution ----------
 
 def main_2(rray):
    steps = array[0]
    jumps = 0
    max_reach = array[0]

    for i in range(0, len(array) - 1):
        max_reach = max(max_reach, array[i] + i)
        steps = steps - 1
        if steps == 0:
            jumps = jumps + 1
            steps = max_reach - i

    return jumps + 1
 
