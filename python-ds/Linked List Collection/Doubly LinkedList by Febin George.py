class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def insert_end(self, data):
        new_node = Node(data)

        if self.head.next is None:
            self.head.next = new_node
            return

        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def insert_start(self, data):
        new_node = Node(data)

        if self.head.next is None:
            self.head.next = new_node
            return

        current_node = self.head.next
        new_node.next = current_node
        current_node.prev = new_node

        self.head.next = new_node

    def insert_at(self, position, data):
        # assert 0 <= position <= self.list_length() - 1, "List index out of range"

        if position == 0:
            li.insert_start(data)
            return
        elif position == li.list_length():
            li.insert_end(data)
            return

        new_node = Node(data)

        index = 0
        previous_node = self.head
        current_node = previous_node.next

        while current_node is not None:
            if index == position:
                new_node.next = current_node
                current_node.prev = new_node

                previous_node.next = new_node
                new_node.prev = previous_node
                break
            index += 1
            previous_node = current_node
            current_node = current_node.next

    def insert_before(self, data, new_data):
        new_node = Node(new_data)
        previous_node = self.head
        current_node = previous_node.next

        while current_node is not None:
            if current_node.data == data:
                new_node.next = current_node
                current_node.prev = new_node

                previous_node.next = new_node
                new_node.prev = previous_node
                break
            previous_node = current_node
            current_node = current_node.next

    def insert_after(self, data, new_data):
        new_node = Node(new_data)
        previous_node = self.head
        current_node = previous_node.next

        while current_node is not None:
            if current_node.data == data:
                new_node.next = current_node.next
                current_node.next = new_node
                new_node.prev = current_node

                if new_node.next is None:
                    break
                current_node.next.prev = new_node

                break
            previous_node = current_node
            current_node = current_node.next

    def print_list(self):
        print()
        if self.is_empty():
            print("List is empty")
            return

        current_node = self.head.next
        while current_node is not None:
            print(current_node.data, end=" => ")
            current_node = current_node.next

    def list_length(self):
        size = 0
        current_node = self.head.next
        while current_node is not None:
            current_node = current_node.next
            size += 1
        return size

    def is_empty(self):
        if self.head.next is None:
            return True
        return False


li = DoublyLinkedList()
li.insert_end("A")
li.insert_end("B")
li.insert_end("C")
li.insert_end("D")
li.insert_end("E")
li.print_list()

li.insert_start("M")
li.insert_start("L")
li.insert_start("K")
li.print_list()
print()
print(li.list_length())
li.insert_at(0, "P")
# li.insert_at(4, "Q")
# li.insert_at(7, "R")
# li.insert_at(8, "S")
li.print_list()
print()
li.insert_before("K", "N")
li.insert_before("P", "T")
li.insert_before("E", "Z")
li.print_list()
print()
li.insert_after("E", "U")
li.print_list()
