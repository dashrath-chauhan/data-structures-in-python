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

class cll:
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
            if currNode == self.head:
                break
            

    def addBeginning(self,data):
        newNode = Node(data)
        currNode = self.head
        newNode.next = self.head
        if self.head is None:
            newNode.next = newNode
            self.length += 1
        else:
            while currNode.next != self.head:
                currNode = currNode.next

            currNode.next = newNode
            self.length += 1
            
        self.head = newNode
        
    def addLast(self,data):
        newNode = Node(data)
        
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.length += 1
        else:
            currNode = self.head
            while currNode.next != self.head:
                currNode = currNode.next
                
            currNode.next = newNode 
            newNode.next = self.head
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
        if currNode.next == self.head:
            self.head = None
            self.length -= 1
        else:
            while currNode.next != self.head:
                currNode = currNode.next

            currNode.next = self.head.next
            self.head = self.head.next
            self.length -= 1

    def deleteLast(self):
        if self.head is None:
            return
    
        currNode = self.head
        prevNode = None
        if currNode.next == currNode:
            self.head = None
            self.length -= 1
        else:
            while currNode.next != self.head:
                prevNode = currNode
                currNode = currNode.next
            
            prevNode.next = currNode.next
            self.head = prevNode.next
            self.length -= 1

    
    def delete_node(self,data):
        if self.head.data == data:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            self.length -= 1
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr.data == data:
                    prev.next = curr.next
                    curr = curr.next
            self.length -= 1

    def delete_nodee(self,node):
        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            self.length -= 1
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr == node:
                    prev.next = curr.next
                    curr = curr.next
            self.length -= 1

    def jproblem(self,k):
        curr = self.head
        
        while self.length > 1:
            count = 1
            while k != count:
                curr = curr.next
                count += 1
            print("Removed:"+str(curr.data))
            self.delete_nodee(curr)
            curr = curr.next

            
cll = cll()
cll.addBeginning(40)
cll.addBeginning(30)
cll.addBeginning(20)
cll.addBeginning(10)
#cll.addMiddle(cll.head.next.next,100)
cll.printList()
cll.jproblem(2)
cll.printList()



