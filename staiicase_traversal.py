# Time: O(height * max_steps)
# Space: O(height)


def main(height, max_steps):
    if height == 1 or height == 0:
        return 1

    steps = [1, 1]

    for i in range(2, height + 1):
        ways = sum(steps[max(0, i-max_steps):i])
        steps.append(ways)
    return steps[-1]
