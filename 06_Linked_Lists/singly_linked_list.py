# CRT Program 27: Create a singly linked list and insert nodes at the end

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
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
size = int(input("Enter number of nodes: "))

for index in range(size):
    value = int(input(f"Enter value {index + 1}: "))
    linked_list.insertion(value)

linked_list.display()
