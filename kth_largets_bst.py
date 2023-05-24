class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self


a = BST(15).insert(20).insert(22).insert(17).insert(5).insert(5).insert(2).insert(3).insert(1).insert(24).insert(21).insert(23)



def traverse_tree_right(tree, stack):
    if tree.right is not None:
        stack.append(tree.right)
        return traverse_tree_right(tree.right, stack)
    return None



def main(tree, k):
    if k == 1:
        return tree.value
    stack = []
    traverse_tree_right(tree, stack)
    largest = []
    for idx, tree in enumerate(reversed(stack)):
        largest.append(tree.value)
        if tree.left:
            largest.append(tree.left.value)

    return largest[k-1]
