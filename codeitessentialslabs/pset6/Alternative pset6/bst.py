'''
    - We have modified TreeNode such that it’s value contains a list. This is because for any rating (overall / potential) there can be multiple players with that rating
    - We have implemented the BST insert method for you, with one modification: if you are inserting a player with the same key, you append it to the node’s value list
'''

class TreeNode():
    def __init__(self, key, value):
        self.key = key
        self.value = [value]
        self.right = None
        self.left = None

class BST():
    def __init__ (self):
        self.root = None
        self.size = 0

    def searchHelper(self, node, item):
        if node == None:
            return None
        elif item == node.key:
            return node
        elif item < node.key:
            return self.searchHelper(node.left, item)
        elif item > node.key:
            return self.searchHelper(node.right, item)

    def search(self, item):
        return self.searchHelper(self.root, item)

    def insertHelper(self, node, newKey, newValue):
        if node == None:
            self.size += 1
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