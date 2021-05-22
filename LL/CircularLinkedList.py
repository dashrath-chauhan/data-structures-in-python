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
        self.length = 0
        
    def print_list(self):
        currNode = self.head
        
        while currNode:
            print(currNode.data)
            currNode = currNode.next
            if currNode == self.head:
                break

        print("\n")

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            self.length += 1
        else:
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next

            new_node = Node(data)
            last_node.next = new_node
            new_node.next = self.head
            self.length += 1

    def prepend(self,data):
        new_node = Node(data)
    
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next

            curr.next = new_node
            new_node.next = self.head
            
        self.head = new_node
        self.length += 1

    def remove(self,key):
        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            curr = self.head    
            while curr and curr.data != key:
                prev = curr
                curr = curr.next

            prev.next = curr.next
            curr = None
        self.length -= 1

    def remove_node(self,node):
        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            curr = self.head    
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr == node:
                    prev.next = curr.next
                    curr = curr.next
        self.length -= 1
		
	def remove_node(self,node):
		if node == self.head:
			curr = self.head
			while curr.next != self.head:
				curr = curr.next
				
			prev.next = self.head.next
			self.head = self.head.next
		else:
			prev = None
			curr = self.head
			while curr.next != self.head:
				prev = curr
				curr = curr.next
				if curr == node:
					prev.next = curr.next
					curr = curr.next
					
    def josephus_problem(self,step):
        curr = self.head

        while self.length > 1:
            count = 1
            while count != step:
                curr = curr.next
                count += 1
            print("Removed: ",str(curr.data))
            self.remove_node(curr)
            curr = curr.next
    
cill = cll()
cill.append("C")
cill.append("D")
cill.prepend("B")
cill.prepend("A")
cill.print_list()
cill.append("E")
cill.append("F")
cill.append("G")
cill.print_list()
print(cill.length)
cill.josephus_problem(3)
cill.print_list()


















