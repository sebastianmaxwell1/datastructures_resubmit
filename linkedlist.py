from node import *


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next



linked_list = LinkedList()
linked_list.append_node(60)
linked_list.append_node(70)
linked_list.append_node(80)
linked_list.prepend_node(40)

