# CRT Program 30: Insert a node at a specified position in a singly linked list
# Positions are 1-based: position 1 means the beginning.

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

    def insertion_at_position(self, value, position):
        if position < 1:
            raise ValueError("Position must be 1 or greater.")

        new_node = Node(value)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return

        current = self.head
        current_position = 1

        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None:
            raise IndexError("Position is outside the list.")

        new_node.next = current.next
        current.next = new_node

        if new_node.next is None:
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

new_value = int(input("Enter value to insert: "))
position = int(input("Enter position (starting from 1): "))

try:
    linked_list.insertion_at_position(new_value, position)
    linked_list.display()
except (ValueError, IndexError) as error:
    print("Insertion failed:", error)
