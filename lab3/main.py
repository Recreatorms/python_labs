class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    __stack = []

    def __init__(self, root):
        current = root
        while current is not None:
            self.__stack.append(current)
            current = current.left

    def current(self):
        return self.__stack[-1]

    def insert(self, value):
        if not self.value:
            self.value = value
            return
        if self.value == value:
            return
        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = BinarySearchTree(value)
            return
        if self.right:
            self.right.insert(value)
            return
        self.right = BinarySearchTree(value)

    # inorder
    def next(self):
        current = self.current().right
        self.__stack.pop()
        while current is not None:
            self.__stack.append(current)
            current = current.left

    def __iter__(self):
        yield 


root = BinarySearchTree(Node(1))
root.insert(10)
# root.insert(Node(15))
# root.insert(Node(5))
# root.insert(Node(2))

for i in root:
    print(i, end=" ")
print()