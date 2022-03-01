class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def is_empty(self):
        current_node = self.head.next
        if current_node is None:
            return True
        return False

    def list_length(self):
        current_node = self.head.next
        count = 0

        while current_node is not None:
            current_node = current_node.next
            count += 1
        return count

    def insert_end(self, new_node):
        # head=>John->None
        if self.head is None:
            self.head = new_node  # making 'new_node' as the 'head_node'
        else:
            # head=>John->Ben->None
            # self.head.next = new_node  # not a good solution
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def insert_head(self, new_node):
        # # data => George, next => None
        # temp_node = self.head  # Matthew
        # # self.head = new_node  # George
        # # self.head.next = temp_node
        # del temp_node

        # # # second rule
        current_node = self.head
        new_node.next = current_node.next
        current_node.next = new_node

    def insert_at(self, new_node, position):
        # head => 10 => 20 => 30 => None
        # new_node => 15-> None
        # position => 2

        # if position == 0:
        #     self.insert_head(new_node)

        if position < 0 or position > self.list_length():
            print("Invalid position")
            return

        previous_node = self.head
        current_node = self.head.next
        current_position = 0  # 0, 1, 2

        while True:

            if current_position == position:
                new_node.next = current_node
                previous_node.next = new_node
                break
            # previous_node = current_node
            previous_node = previous_node.next
            current_node = current_node.next
            current_position += 1

    def delete_end(self):

        if self.is_empty():
            print("List is empty. No item to delete.")
            return

        # previous_node = self.head
        current_node = self.head.next

        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = None

    def delete_head(self):
        previous_node = self.head
        current_node = self.head.next

        # if current_node is None:
        if self.is_empty():
            print("List is empty")
            return
        previous_node.next = current_node.next
        current_node.next = None

    def delete_at(self, position):
        if position < 0 or position >= self.list_length():
            print()
            print("list index out of range")
            return
        previous_node = self.head
        current_node = self.head.next

        current_index = 0
        while current_node is not None:
            if current_index == position:
                previous_node.next = current_node.next
                current_node.next = None
                return
            previous_node = previous_node.next
            current_node = current_node.next
            current_index += 1

    def print_list(self):
        print()
        # head=>John->Ben->Matthew
        current_node = self.head.next
        if current_node is None:
            print("linked list is empty")
            return

        while current_node is not None:
            print(current_node.data, end=" => ")
            current_node = current_node.next


# # ==========================================================
# # 01-02

# li = LinkedList()

# first_node = Node("John")
# li.insert_end(first_node)
#
# second_node = Node("Ben")
# li.insert_end(second_node)
#
# third_node = Node("Matthew")
# li.insert_end(third_node)
#
# li.print_list()

# # =========================================================
# # 03-04

# li = LinkedList()
#
# first_node = Node("John")
# li.insert_end(first_node)
#
# second_node = Node("Ben")
# li.insert_end(second_node)
#
# third_node = Node("Matthew")
# li.insert_end(third_node)
#
# fourth_node = Node("George")
# li.insert_head(fourth_node)
#
# li.print_list()


# # ==========================================================
# # 05-06

# li = LinkedList()
#
# first_node = Node(10)
# li.insert_end(first_node)
#
# second_node = Node(20)
# li.insert_end(second_node)
#
# third_node = Node(30)
# li.insert_end(third_node)
#
# li.print_list()
# fourth_node = Node(40)
# li.insert_head(fourth_node)
#
# li.print_list()
# #
# fifth_node = Node(15)
# # li.insert_at(fifth_node, 2)
# # li.insert_at(fifth_node, 0)
# li.insert_at(fifth_node, 3)
# # li.insert_at(fifth_node, 4)
# print()
# # li.insert_at(fifth_node, -1)
#
# li.print_list()
#
# size = li.list_length()
# print()
# # print(f"Number of elements: {size}")

# # # ==========================================================
# # 07-08 code for deleting last node
#
# li = LinkedList()
#
# first_node = Node(10)
# li.insert_end(first_node)
#
# second_node = Node(20)
# li.insert_end(second_node)
#
# third_node = Node(30)
# li.insert_end(third_node)
#
# fourth_node = Node(40)
# li.insert_head(fourth_node)
#
# fifth_node = Node(15)
# li.insert_at(fifth_node, 3)
# print()
#
# li.print_list()
# li.delete_end()
# li.print_list()

# # ==========================================================
# # 09-10 deleting head node
# li = LinkedList()
#
# first_node = Node(10)
# li.insert_end(first_node)
#
# second_node = Node(20)
# li.insert_end(second_node)
#
# third_node = Node(30)
# li.insert_end(third_node)
#
# fourth_node = Node(40)
# li.insert_head(fourth_node)
#
# fifth_node = Node(15)
# li.insert_at(fifth_node, 3)
# li.print_list()
#
# li.delete_head()
# li.print_list()
#
# li.delete_head()
# li.print_list()
# print()

# print(f"is_empty: {li.is_empty()}")

# # # ==========================================================
# # # 11-12 deleting a node in between two other nodes
#
# li = LinkedList()
#
# first_node = Node(10)
# li.insert_end(first_node)
#
# second_node = Node(20)
# li.insert_end(second_node)
#
# third_node = Node(30)
# li.insert_end(third_node)
#
# fourth_node = Node(40)
# li.insert_head(fourth_node)
#
# fifth_node = Node(15)
# li.insert_at(fifth_node, 3)
# li.print_list()
#
# # print(li.list_length())
#
# li.delete_at(2)
# li.print_list()


