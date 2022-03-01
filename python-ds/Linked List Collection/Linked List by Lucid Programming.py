# # 05 singly linked list - insertion


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def print_list(self):
        current_node = self.head.next
        while current_node is not None:
            print(current_node.data, end=" => ")
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head.next is None:
            self.head.next = new_node
            return

        current_node = self.head
        # while current_node.next is not None:
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert_after(self, prev_node, data):
        # if not prev_node:
        # # # for debugging purpose
        # print(prev_node.data)
        # print(prev_node.next.data)

        if prev_node is None:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        # # MY IMPLEMENTATION
        previous_node = self.head
        current_node = previous_node.next
        while current_node is not None:
            if current_node.data == key:
                previous_node.next = current_node.next
                current_node.next = None
                break
            previous_node = current_node
            current_node = current_node.next

    def delete_at(self, position):
        assert 0 <= position <= self.list_length() - 1, "List index out of range."
        index = 0
        previous_node = self.head
        current_node = previous_node.next

        while current_node is not None:
            if index == position:
                previous_node.next = current_node.next
                current_node.next = None
                break
            previous_node = current_node
            current_node = current_node.next
            index += 1

    def list_length(self):
        size = 0
        current_node = self.head.next

        while current_node is not None:
            current_node = current_node.next
            size += 1

        return size

    def list_length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.list_length_recursive(node.next)

    def is_empty(self):
        if self.head.next is None:
            return True
        return False


li = LinkedList()
# # ==========================================================
# # append()

li.append("A")
li.append("B")
li.append("C")
li.append("D")
# li.print_list()
print()
# # ==========================================================
# # prepend()

li.prepend("E")
# li.print_list()
# print()
li.prepend("K")
# li.print_list()
# print()

# # ==========================================================
# # insert_after()

# # print(li.head.data)
# # print(li.head.next.data)
# # li.insert_after(li.head, "L")
li.insert_after(li.head.next, "L")
# # li.insert_after(li.head.next.next, "L")
# li.print_list()
# print()

# # ==========================================================
# # delete_node()

# li.delete_node("B")
# li.delete_node("K")
# li.delete_node("D")
li.delete_node("E")
li.print_list()
# print()
# li.delete_node("A")
# li.print_list()
print()

# # # ==========================================================
# # # delete_at()
#
# li.delete_at(3)
# li.print_list()

# # # ==========================================================
# # # list_length()
#
# print()
# print(li.list_length())

# # # ==========================================================
# # # list_length_recursive()
# #
# print()
# print(li.list_length_recursive(li.head.next))

# # # ==========================================================
# # # is_empty()
#
# print(li.is_empty())
#
# li2 = LinkedList()
# print(li2.is_empty())
