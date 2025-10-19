class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def append_back(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next

    #Additional to the task function
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_pos = current.next
            current.next = previous
            previous = current
            current = next_pos

        self.head = previous

l = LinkedList()
l.append_back(1)
l.append_back(2)
l.append_back(3)
l.append_back(4)
l.append_back(5)
print(l.display())
l.reverse()
print(l.display())