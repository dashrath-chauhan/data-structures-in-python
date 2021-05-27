"""
a tree which has atmost two child

in binary search tree unlike binary tree values are in specific order
like left child of root has to be less than root
and, right child of the root has to be greater than root
Input - 8 3 10 1 6, create binary tree
        8
       / \
      3   10
     / \
    1   6
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,currNode):
        if data < currNode.data:
            if currNode.left is None:
                currNode.left = Node(data)
            else:
                self._insert(data,currNode.left)
        elif data > currNode.data:
            if currNode.right is None:
                currNode.right = Node(data)
            else:
                self._insert(data,currNode.right)
        else:
            print('Value already in tree')
            return

    def print_tree(self,root):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self,curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left)
            print(curr_node.data)
            self._print_tree(curr_node.right)

    def find(self,data):
        if self.root:
            isFound = self._find(data,self.root)
            if isFound:
                return True
            return False
        else:
            return None

    def _find(self,data,currNode):
        if data < currNode.data and currNode.left:
            return self._find(data,currNode.left)
        elif data > currNode.data and currNode.right:
            return self._find(data,currNode.right)
        if data == currNode.data:
            return True

bst = BST()
bst.insert(8)
bst.insert(6)
bst.insert(1)
bst.insert(10)
bst.insert(9)
bst.insert(7)
bst.insert(3)
bst.print_tree(bst)
print(bst.find(8))















                
