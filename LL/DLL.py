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
head.next.next.next.next.next = head
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
        self.prex = None

class dll:
    def __init__(self):
        self.head = None
        #self.tail = None
        self.length = 0
        
    def printList(self):
        currNode = self.head
        
        print(self.length)
        while currNode:
            print(currNode.data)
            currNode = currNode.next
            

    def addBeginning(self,data):
        newNode = Node(data)
        
        if self.head is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.length += 1
        else:
            newNode.prev = None
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.length += 1
            
        
    def addLast(self,data):
        newNode = Node(data)
        
        if self.head is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
            self.length += 1
        else:
            currNode = self.head
            while currNode.next:
                currNode = currNode.next

            currNode.next = newNode
            newNode.prev = currNode
            newNode.next = None
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
        currNode = self.head
        if currNode.next == None and currNode.prev == None:
            self.head = None
            self.length -= 1
        else:
            self.head = currNode.next
            currNode.next = None
            self.length -= 1

    def deleteLast(self):
        if self.head is None:
            return
        currNode = self.head
        prevNode = None
        if currNode.next == None and currNode.prev == None:
            self.head = None
            self.length -= 1
        else:
            while currNode.next:
                prevNode = currNode
                currNode = currNode.next
            
            prevNode.next = None
            self.length -= 1

        
dll = dll()
dll.addLast(10)
dll.addLast(20)
dll.addLast(30)
dll.addBeginning(40)
dll.addBeginning(50)
#cll.addMiddle(cll.head.next.next,100)
dll.printList()
dll.deleteFirst()
dll.printList()
dll.deleteLast()
dll.deleteLast()
dll.printList()



