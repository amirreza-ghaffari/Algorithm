class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self
        
 
 
 test_tree = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22).insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000).insert(204).insert(205).insert(207).insert(206).insert(208).insert(203).insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)


def main(tree, target_value):
    return search_in_tree(tree, target_value, float('inf'))


def search_in_tree(tree, target_value, closest_value):
    if tree is None:
        return closest_value

    if abs(tree.value - target_value) < abs(closest_value - target_value):
        closest_value = tree.value
    if target_value > tree.value:
        return search_in_tree(tree.right, target_value, closest_value)
    elif target_value < tree.value:
        return search_in_tree(tree.left, target_value, closest_value)
    else:
        return closest_value
