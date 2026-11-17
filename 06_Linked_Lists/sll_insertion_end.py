# CRT Program 29: Insert a node at the end of a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insertion_at_end(self, value):
        # The tail pointer makes end insertion efficient.
        self.insertion(value)

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
size = int(input("Enter number of initial nodes: "))

for index in range(size):
    value = int(input(f"Enter value {index + 1}: "))
    linked_list.insertion(value)

new_value = int(input("Enter value to insert at the end: "))
linked_list.insertion_at_end(new_value)
linked_list.display()
