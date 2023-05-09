# Time: O(N^2)
# Space: O(1)



def check_palindrome(string, i):
    counter = 1
    longest_odd = string[i]
    longest_even = ""
    even_flag = True
    odd_flag = True
    while i - counter >= 0 and i + counter <= len(string) - 1:
        if string[i - counter] == string[i + counter] and odd_flag:
            longest_odd = string[i-counter] + longest_odd + string[i + counter]
        else:
            odd_flag = False

        if string[i-counter + 1] == string[i + counter] and even_flag:
            longest_even = string[i-counter + 1] + longest_even + string[i+counter]
        else:
            even_flag = False

        if not even_flag and not odd_flag:
            break
        counter = counter + 1
    return longest_even if len(longest_even)> len(longest_odd) else longest_odd


def main(string):
    longest = ""
    for i in range(0, len(string)):
        longest_iterate = check_palindrome(string, i)
        print(longest_iterate)
        if len(longest_iterate) > len(longest):
            longest = longest_iterate
    return longest








