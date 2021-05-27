

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
            self._insert(self.root,data)

    def _insert(self,root,data):
        if data < root.data:
            if root.left:
                self._insert(root.left,data)
            else:
                root.left = Node(data)
        elif data > root.data:
            if root.right:
                self._insert(root.right,data)
            else:
                root.right = Node(data)
        else:
            return
            
    def find(self,data):
        if self.root:
            is_found = self._find(self.root,data)
            return is_found
        else:
            return None

    def _find(self,root,data):
        if data < root.data and root.left:
            return self._find(root.left,data)
        elif data > root.data and root.right:
            return self._find(root.right,data)
        elif root.data == data:
            return True
        
    def delete(self):
        pass
    
    def pre_order(self,root):
        if root is None:
            return
        else:
            print(str(root.data)+" - ", end="")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self,root):
        if root is None:
            return
        else:
            self.in_order(root.left)
            print(str(root.data)+" - ", end="")
            self.in_order(root.right)

    def post_order(self,root):
        if root is None:
            return
        else:
            self.post_order(root.left)
            self.post_order(root.right)
            print(str(root.data)+" - ", end="")

        
class BTree:
    def __init__(self,root):
        self.root = Node(root)

    def pre_order(self,root):
        if root is None:
            return
        else:
            print(str(root.data)+" - ", end="")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self,root):
        if root is None:
            return
        else:
            self.in_order(root.left)
            print(str(root.data)+" - ", end="")
            self.in_order(root.right)

    def post_order(self,root):
        if root is None:
            return
        else:
            self.post_order(root.left)
            self.post_order(root.right)
            print(str(root.data)+" - ", end="")

tree = BTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
'''print("\nPre-order:")
tree.pre_order(tree.root)
print("\nIn-order")
tree.in_order(tree.root)
print("\nPost-order")
tree.post_order(tree.root)
'''
bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
print("\nPre-order:")
bst.pre_order(bst.root)
print("\nIn-order")
bst.in_order(bst.root)
print("\nPost-order")
bst.post_order(bst.root)
print("\n"+str(bst.find(5)))
print(bst.find(6))












