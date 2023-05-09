#Implement a function that returns the longest subsequence common to two given strings. 
#A subsequence is defined as a group of characters that appear sequentially, with no importance given to their actual position in a string. 
#In other words, characters do not need to appear consecutively in order to form a subsequence. Assume that there will only be one longest common subsequence.


# Time: O(n*M + Min(m,n))
# Space: O(n*M + Min(m,n))

def main(str1, str2):
    mask = [["" for j in range(0, len(str2) + 1)] for i in range(0, len(str1) + 1)]

    for j in range(1, len(str2) + 1):
        for i in range(1, len(str1) + 1):
            if str1[i - 1] == str2[j - 1]:
                mask[i][j] = mask[i - 1][j - 1] + str1[i - 1]
            else:
                temp1 = mask[i - 1][j]
                temp2 = mask[i][j - 1]
                mask[i][j] = temp1 if len(temp1) > len(temp2) else temp2
    return mask[-1][-1]
