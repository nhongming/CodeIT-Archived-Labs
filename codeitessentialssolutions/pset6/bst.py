class TreeNode():
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.right = None
        self.left = None


class BST():
    def __init__(self):
        self.root = None
        self.size = 0

    def insertHelper(self, node, newKey, newValue):
        if node == None:
            return TreeNode(newKey, newValue)
        elif newKey == node.key:
            node.value.append(newValue)
            return node
        elif newKey < node.key:
            node.left = self.insertHelper(node.left, newKey, newValue)
        elif newKey > node.key:
            node.right = self.insertHelper(node.right, newKey, newValue)
        return node

    def insert(self, newKey, newValue):
        self.root = self.insertHelper(self.root, newKey, newValue)
