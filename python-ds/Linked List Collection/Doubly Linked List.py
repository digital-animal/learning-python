class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)

        # if the list is empty
        if self.head.next is None:
            self.head.next = new_node
            return

        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head.next is None:
            self.head.next = new_node
            return

        previous_node = self.head
        current_node = previous_node.next

        new_node.next = current_node
        current_node.prev = new_node

        previous_node.next = new_node

    def insert_at(self, data, position):
        new_node = Node(data)

        previous_node = self.head
        current_node = previous_node.next

        index = 0
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

    def remove_at_index(self, position):
        previous_node = self.head
        current_node = previous_node.next

        index = 0
        while current_node is not None:
            if index == position:
                previous_node.next = current_node.next
                if previous_node.next is None:
                    break
                current_node.next.prev = previous_node
                break
            index += 1
            previous_node = current_node
            current_node = current_node.next

    def remove_item(self, item):

        previous_node = self.head
        current_node = previous_node.next
        next_node = current_node.next

        while current_node is not None:
            if current_node.data == item:
                previous_node.next = next_node
                current_node.next = None
                if previous_node.next is None:
                    break
                next_node.prev = previous_node
                break
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next

    def search(self, key):
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

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

    def print_list(self):
        current_node = self.head.next

        while current_node is not None:
            print(current_node.data, end=" => ")
            current_node = current_node.next


li = DoublyLinkedList()
li.append(4)
li.append(9)
li.append(2)
li.append(3)
li.append(5)
# print()
# li.print_list()
print()
li.prepend(11)
li.prepend(13)
li.prepend(17)
li.prepend(19)
li.print_list()
print()
# print(li.search(4))
# print(li.search(7))
# print(li.is_empty())
# print(li.list_length())
# li.remove_index(5)
# li.remove_at_index(0)
# li.remove_at_index(4)
# li.remove_at_index(7)
# li.remove_at_index(8)
# li.print_list()
# print()
# li.insert_at(23, 6)
# li.print_list()
# li.remove_item(5)
# li.remove_item(19)
# li.remove_item(3)
li.print_list()