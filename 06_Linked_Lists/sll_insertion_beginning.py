# CRT Program 28: Insert a node at the beginning of a singly linked list

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

    def insertion_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

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

new_value = int(input("Enter value to insert at the beginning: "))
linked_list.insertion_at_beginning(new_value)
linked_list.display()
