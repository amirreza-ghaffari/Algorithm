# Time: O(N)
# Space: O(N)

# -----------with only one for loop -----------
def main(string):
    out = ""
    j = len(string) - 1

    while j >= 0:
        if string[j] == ' ':
            out = out + ' '
            j = j - 1
        else:
            temp_idx = j
            while string[j] != ' 'and j >=0:
                j = j-1
            out = out + string[j+1:temp_idx+1]

    return out
