"""
a tree which has atmost two child

"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)
        
    #root -> left -> right
    def pre_order(self, root):
        traversal = ""
        if root:
            traversal += (str(root.data) + "-")
            traversal += self.pre_order(root.left)
            traversal += self.pre_order(root.right)

        return traversal
            
    #left -> right -> root
    def post_order(self, root):
        traversal = ""
        if root:
            traversal += self.post_order(root.left)
            traversal += self.post_order(root.right)
            traversal += (str(root.data) + "-")

        return traversal

    #left -> root -> right
    def in_order(self, root):
        traversal = ""
        if root:
            traversal += self.in_order(root.left)
            traversal += (str(root.data) + "-")
            traversal += self.in_order(root.right)

        return traversal

    def height(self,root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height,right_height)
                
    def size(self):
        if self.root is None:
            return 0

        s = Stack()
        s.push(self.root)
        size = 1
        while stack:
            node = s.pop()
            if node.left:
                size += 1
                s.push(node.left)
            if node.right:
                size += 1
                s.push(node.right)

        return size
                

btree = BinaryTree(1)
btree.root.left = Node(2)
btree.root.right = Node(3)
btree.root.left.left = Node(4)
btree.root.left.right = Node(5)
btree.root.right.left = Node(6)
btree.root.right.right = Node(7)
btree.root.right.right.right = Node(8)
print("Preorder:\t",btree.pre_order(btree.root))
print("Postorder:\t",btree.post_order(btree.root))
print("Inorder:\t",btree.in_order(btree.root))
print(btree.height(btree.root))
print(btree.size())













                
