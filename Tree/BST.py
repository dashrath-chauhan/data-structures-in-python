


class Node:
    def __init__(self,data=None):
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
            self._insert(data, self.root)

    def _insert(self,data,curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data,curr_node.left)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data,curr_node.right)
        else:
            print(data," already in tree")

    def find(self,data):
        if self.root:
            is_found = self._find(data,self.root)

        return is_found

    def _find(self,data,curr_node):
        if data == curr_node.data:
            return True
        if data < curr_node.data and curr_node.left:
            return self._find(data,curr_node.left)
        elif data > curr_node.data and curr_node.right:
            return self._find(data,curr_node.right)
        else:
            return False
        
    def inorder(self):
        if self.root:
            return self._inorder(self.root)

    def _inorder(self,curr_node):
        traversal = ""

        if curr_node:
            traversal += self._inorder(curr_node.left)
            print(curr_node.data)
            traversal += self._inorder(curr_node.right)

        return traversal

    # Helper function to find minimum value node in subtree rooted at curr
    def minimumKey(curr):
        while curr.left:
            curr = curr.left
 
        return curr

    def delete_node(self,data):
        parent = None
        curr = self.root
        
        while curr and curr.data != data:
            parent = curr
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return data,"not in tree"

        # case 1: not left or right child to a node
        if curr.left is None and curr.right is None:
            if curr != self.root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right =  None
            else:
                self.root = None

        #case2: if node has left and right child
        elif curr.right and curr.left:
            #get successor of current node to be deleted
            successor = minimum_key(curr.right)

            #store value of successor, later assign it to new node
            val = successor.data
            delete_node(successor.data)

            #assigne value of successor to new node that replaces the deleted node
            curr.data = val

        #case3: if node has only one child
        else:
            if curr.left:
                new_node = curr.left
            else:
                new_node = curr.right

            if curr != self.root:
                if curr == parent.left:
                    parent.left = new_node
                else:
                    parent.right = new_node
            else:
                self.root = new_node

        return self.root
    
bst = BST()
bst.insert(8)
bst.insert(10)
bst.insert(3)
bst.insert(6)
bst.insert(7)
print(bst.find(6))
print(bst.root.data)
print(bst.inorder())
bst.delete_node(6)
print(bst.inorder())
print(bst.root.data)













