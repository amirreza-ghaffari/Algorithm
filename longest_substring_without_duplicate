#  Time: O(N)
#  Space: O(min(A, alphabet_lenght))

def main(string):
    idx = 0
    t = {}
    longest = [0, 1]
    for i, char in enumerate(string):
        if char in t:
            idx = max(idx, t[char] + 1)
        if longest[1] - longest[0] < i + 1 -idx:
            longest = [idx, i+1]
        t[char] = i
