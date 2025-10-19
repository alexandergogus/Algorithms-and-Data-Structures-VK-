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
    def search_middle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

l = LinkedList()
l.append_back(3)
l.append_back(8)
l.append_back(9)
l.append_back(6)
l.append_back(11)
l.append_back(16)
l.append_back(17)
middle = l.search_middle()
print(middle.data)