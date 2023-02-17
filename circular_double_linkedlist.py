class Node: # Node construct
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Circular_Double_Linklist:
    def __init__(self, head=None): # linklist attributes
        self.head = head
        self.tail = None
        self.length = 0

    def add_end(self, data):
        """Adds a node to the end of our circular double linklist in O(1)"""
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.tail.next, self.head.prev = self.head, self.tail

        self.length += 1

    def add_front(self, data):
        """Adds a node to the beginning of our circular double linklist in O(1)"""
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head, self.head.next= Node(data), self.head
            self.head.next.prev = self.head
            self.head.prev, self.tail.next = self.tail, self.head
        
        self.length += 1
        
    def add_at_position(self, data, index):
        """Adds a node a to stipulated position in our Circular Double Linklist in O(n)"""
        if index == 0:
            self.add_front(data)
        else:
            current_position = 0
            previous_node = None
            current_node = self.head
            
            while current_position != index:
                previous_node = current_node
                current_node = current_node.next
                current_position += 1
                
            previous_node.next = Node(data)
            previous_node.next.prev = previous_node
            previous_node.next.next = current_node
        
        self.length += 1
                

    def delete_node(self, data):
        """deletes a stipulated node from the Circular Double Linklist in O(n)"""
        if self.head.data is data:
            self.head = self.head.next
            self.head.prev = None
        else:
            current_node = self.head
            previous_node = None
        
            while current_node.data is not data:
                previous_node = current_node
                current_node = current_node.next
                
            previous_node.next = current_node.next
            current_node.next.prev = previous_node
            
        self.length -= 1

    def traverse_farward(self):
        """Traverse the linklist from the head down"""
        current_node = self.head
        counter = 0
        while counter < 15:
            print(current_node.data, end=" => ")
            current_node = current_node.next
            counter += 1
    
    def traverse_backward(self):
        """Traverse the linklist from the tail up"""
        current_node = self.tail
        counter = 0
        while counter < 15:
            print(current_node.data, end=" => ")
            current_node = current_node.prev
            counter += 1
        
        print(None)

    def get_length(self):
        """Returns the length of the 
        Circular Double Linklist"""
        return self.length

#circular double linklist instance
CDL = Circular_Double_Linklist()
CDL.add_front(53)
CDL.add_front(82)
CDL.add_front(59)
CDL.add_at_position(65, 2)

print("Farward Traveral:")
CDL.traverse_farward()
print("\nBackward Traversal:")
CDL.traverse_backward()
print("Length of linklist:",CDL.get_length())
