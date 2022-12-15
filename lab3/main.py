class BinarySearchTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add_element(self, value):
        # if the tree is empty
        if self.value is None:
            self.value = value

        elif value < self.value:
            if self.left is not None:
                self.left.add_element(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right is not None:
                self.right.add_element(value)
            else:
                self.right = BinarySearchTree(value)

    def __iter__(self):
        if self.left:
            yield from self.left.__iter__()

        yield self.value

        if self.right:
            yield from self.right.__iter__()


tree = BinarySearchTree()

tree_nodes = [1, 200, 1000, 350, 5, 10, 15, 20, 50, 100, 250]

for iter in tree_nodes:
    tree.add_element(iter)

print()

for iter in tree:
    print(iter)
