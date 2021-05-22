"""

Node: data and adress to next node
only to access element is using head node
In entire list head is the only known node, so everything has to be done using head node
List: 10 20 30 40 50

head is first node in the list
head.data = 10
head.next.data = 20
head.next.next.data = 30
head.next.next.next.data = 40
head.next.next.next.next.data = 50
head.next.next.next.next.next = null
last node is list have data but next pointer is always null, indicating the end of linked list

Boundary conditions:
1. Empty data structure
    when adding element, when deleting element
2. Single element in data structure
    when adding element, when deleting element
3. Adding/Removing from the beginning of the list
    handle head, handle next pointers
4. Adding/Removing from the end of the data structure
    handle last node, handle if first is the last element
5. Working in the middle
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def print_list(self):
        curr_node = self.head
        length = 0
        while curr_node:
            print(curr_node.data)
            length += 1
            curr_node = curr_node.next

        print("Length:",length,"\n")

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if self.head is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self,key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        prev.next = curr_node.next
        curr_node = None

    def node_swap(self,key1,key2):
        prev1 = None
        prev2 = None
        curr1 = self.head
        curr2 = self.head

        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return
        
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1
        
        curr1.next, curr2.next = curr2.next, curr1.next
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    def rotate(self,k):
        p = self.head
        q = self.head
        prev = None
        count = 0

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        
        while q:
            prev = q
            q = q.next
        q = prev
        
        q.next = self.head
        self.head = p.next
        p.next = None

sill = SinglyLinkedList()
sill.append("A")
sill.append("B")
sill.append("C")
sill.prepend("D")
sill.insert_after(sill.head.next.next,"E")
sill.print_list()
sill.delete_node("B")
sill.print_list()
sill.node_swap("A","E")
sill.print_list()
sill.reverse()
sill.print_list()
sill.rotate(1)
sill.print_list()















