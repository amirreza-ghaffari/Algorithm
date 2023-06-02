def main(string):
    stack = []
    t = {'(': ')', '[': ']', '{': '}'}

    if len(string) == 0:
        return True

    for i in range(0, len(string)):
        if a[i] in t:
            stack.append(a[i])
        else:
            if len(stack) == 0:
                return False
            item = stack.pop()
            if t[item] != a[i]:
                return False
    return True
