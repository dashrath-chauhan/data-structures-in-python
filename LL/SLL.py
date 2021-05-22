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
last node is list had data but next pointer is always null, indicating the end of linked list

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

class sll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def printList(self):
        currNode = self.head
        
        print(self.length)
        while currNode:
            print(currNode.data,end=",")
            currNode = currNode.next
        print("\n")
        
    def addBeginning(self,data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return
        
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        
    def addLast(self,data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return

        currNode = self.head
        while currNode.next:
            currNode = currNode.next

        currNode.next = newNode
        self.tail = newNode
        self.length += 1

    def addMiddle(self,prevNode,data):
        if not prevNode:
            return
        
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        self.length += 1

    def deleteFirst(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        
        currNode = self.head
        self.head = currNode.next
        currNode = None
        self.length -= 1

    def deleteLast(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        currNode = self.head
        prevNode = None
        
        while currNode != self.tail:
            prevNode = currNode
            currNode = currNode.next
            
        prevNode.next = None
        self.tail = prevNode
        self.length -= 1

    def node_swap(self,key1,key2):
        if key1 == key2:
            return
        
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

    def print_helper(self,name,node):
        if node is None:
            print(name + ": None")
        else:
            print(name + ": "+str(node.data))

    def reverse_list(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev

            self.print_helper("PREV",prev)
            self.print_helper("CURR",curr)
            self.print_helper("NEXT",nxt)
            print("\n")
            
            prev = curr
            curr = nxt
            
        self.head = prev

    def reverse_list_k(self,head,k):
        prev = None
        curr = head
        count = 0
        nxt = None

        while curr and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1

        if nxt:
            head.next = self.reverse_list_k(nxt,k)
            
        return prev

    def rotate_list(self,k):
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


        
'''sll = sll()
sll.addBeginning(10)
sll.addBeginning(20)
sll.addBeginning(30)
sll.addLast(40)
sll.addMiddle(sll.head.next,50)
sll.printList()
sll.node_swap(10,30)
sll.printList()
sll.reverse_list()
sll.printList()
'''
llist = sll() 
llist.addBeginning(8)
llist.addBeginning(7)
llist.addBeginning(6)
llist.addBeginning(5)
llist.addBeginning(4)
llist.addBeginning(3)
llist.addBeginning(2)
llist.addBeginning(1)
llist.printList()
llist.head = llist.reverse_list_k(llist.head,3)
llist.printList()
llist.rotate_list(4)
llist.printList()







