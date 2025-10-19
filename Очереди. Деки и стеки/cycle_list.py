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

    #Additional function to the question
    def check_cycle(self):
        if self.head is None or self.head.next is None:
            return False
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def create_cycle(self, position):
        if not self.head:
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        cycle_node = self.head
        for i in range(position):
            if cycle_node.next:
                cycle_node = cycle_node.next
            else:
                return

        last_node.next = cycle_node

l = LinkedList()
l.append_back(11)
l.append_back(3)
l.append_back(8)
l.append_back(9)
l.append_back(6)
l.append_back(11)
l.append_back(16)
l.append_back(17)
print(l.check_cycle())
l.create_cycle(2)
print(l.check_cycle())