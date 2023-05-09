# Time: O(N)
# Space: O(depth)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def main(tree):
    return validate(tree, float("-inf"), float("inf"))


def validate(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    left_validation = validate(tree.left, minValue, tree.value)
    right_validation = validate(tree.right, tree.value, maxValue)
    return left_validation and right_validation
