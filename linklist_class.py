# datastructures-algo-python
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self, head=None):
        self.head = head

    def add_head(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp


    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            next_value = self.head
            while True:
                if next_value.next is None:
                    break
                next_value = next_value.next
            next_value.next = Node(data)

    def remove_duplicates(self):
        current_value = self.head
        previous_value = None

        duplicate_value = {}
        while current_value:
            if current_value.data in duplicate_value:
                #remove node
                previous_value.next = current_value.next
                current_value = None
            else:
                #Have not encountered element before
                duplicate_value[current_value.data] = 1
                previous_value = current_value
            current_value = previous_value.next


    def deleteNode(self, data):
        to_delete = Node(data)
        if self.head.data is to_delete.data:
            self.head = self.head.next
           
        else:
            previous_node = self.head
            current_node = self.head
            while True:
                if current_node.data == to_delete.data: 
                    break
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = current_node.next
        return
    

    def display(self):
        while True:
            if self.head is None:
                break
            print(self.head.data," ☞ ", end='')
            self.head = self.head.next 
        print(None)


linklist = LinkList()
# linklist.insert(input())
# linklist.add_head(input())
# linklist.deleteNode(input())
# linklist.remove_duplicates()
linklist.display()