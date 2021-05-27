

"""
Complete binary tree:
In a complete binary tree, every level except possibly the last, is completely filled,
and all odes in the last level are as left as possible

Full binary tree:
a tree in which every node has either 0 or 2 childrens.

Level order traversal
print elements level by level
1 2 3 4 5 6 7
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
1
2 3 -> 1 2
3 4 5 -> 1 2 3
4 5 6 7 -> 1 2 3 4 5
6 7 -> 1 2 3 4 5 6 7
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self,root):
        newNode = Node(root)
        self.root = newNode



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.printTree("preorder"))
print(tree.printTree("inorder"))
print(tree.printTree("postorder"))


























