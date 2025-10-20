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
        print('None')

#Additional to the task functions
def array_to_list(array):
    list0 = LinkedList()
    for i in range(len(array)):
        list0.append_back(array[i])
    return list0

def merge_sorted_lists_inplace(a, b):
    if a.head is None:
        a.head = b.head
        return a
    if b.head is None:
        return a

    if a.head.data <= b.head.data:
        head = a.head
        l1 = a.head.next
        l2 = b.head
    else:
        head = b.head
        l1 = a.head
        l2 = b.head.next

    current = head

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1 is not None:
        current.next = l1
    else:
        current.next = l2

    a.head = head
    return a


a_list = array_to_list([3,6,8])
b_list = array_to_list([4,7,9,11])
merged = merge_sorted_lists_inplace(a_list, b_list)
merged.display()