# Time: O(N)
# Space: O(1)
def main(string):
    string = string.lower()
    string = string.replace(' ', '').replace(',', '').replace(':',  '')
    left_idx = 0
    right_idx = len(string) - 1

    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx = left_idx + 1
        right_idx = right_idx - 1
    return True
