# Time: O(n)
# Space: O(1)
def fibo(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        sum_ = sum(last_two)
        last_two[0] = last_two[1]
        last_two[1] = sum_
        counter = counter + 1
    return last_two[1] if n > 1 else last_two[0]
