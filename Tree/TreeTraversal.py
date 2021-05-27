

"""
Complete binary tree:
In a complete binary tree, every level except possibly the last, is completely filled,
and all nodes in the last level are as left as possible

Full binary tree:
a tree in which every node has either 0 or 2 childrens.

Binary tree traversal:
Traversing/checking each node in a tree exactly once
Tree traversal can be done by Depth First Search and Breadth First Search
Depth First Search:
    -> Preorder traversal -> Root-Left-Right
        check if current node is empty
        display data of root
        traverse left subtree recursively calling the preorder function
        traverse right subtree recursively calling the preorder function
    -> Inorder traversal
        check if current node is empty
        traverse left subtree recursively calling the preorder function
        display data of root
        traverse right subtree recursively calling the preorder function
    -> Postorder traversal
        check if current node is empty
        traverse left subtree recursively calling the preorder function
        traverse right subtree recursively calling the preorder function
        display data of root

1 - 2 - 4 - 5 - 3 - 6 - 7 - preorder 
4 - 2 - 5 - 1 - 6 - 3 - 7 - inorder
4 - 5 - 2 - 6 - 7 - 3 - 1 - postorder
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root,"")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root,"")
        else:
            print("Traversal type not supported")
            return False
        
    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.data) + ' - '
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.data) + ' - '
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.data) + ' - '
        return traversal

tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))


























