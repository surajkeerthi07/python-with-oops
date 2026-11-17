# CRT Program 31: Create and display a doubly linked list

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertion(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


linked_list = DoublyLinkedList()
size = int(input("Enter number of nodes: "))

for index in range(size):
    value = int(input(f"Enter value {index + 1}: "))
    linked_list.insertion(value)

print("Forward:")
linked_list.display_forward()

print("Backward:")
linked_list.display_backward()
