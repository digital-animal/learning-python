class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        current_node = self.head

        new_node = Node(data)

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def prepend(self, data):
        previous_node = self.head
        current_node = self.head.next

        new_node = Node(data)

        new_node.next = previous_node.next

        previous_node.next = new_node

    def print_list(self):
        current_node = self.head.next

        while current_node is not None:
            print(current_node.data, end=" => ")
            current_node = current_node.next

    def insert_after(self, data, new_data):
        previous_node = self.head
        current_node = self.head.next

        new_node = Node(new_data)

        while current_node is not None:
            if current_node.data == data:
                new_node.next = current_node.next
                current_node.next = new_node
                break
            current_node = current_node.next

    def insert_before(self, data, new_data):
        previous_node = self.head
        current_node = self.head.next

        new_node = Node(new_data)

        while current_node is not None:
            if current_node.data == data:
                new_node.next = previous_node.next
                previous_node.next = new_node
                break
            previous_node = previous_node.next
            current_node = current_node.next

    def insert_at(self, index, num):
        previous_node = self.head
        current_node = self.head.next

        new_node = Node(num)
        counter = 0

        while counter <= li.list_length():  # equals because list size increases by 1
            if counter == index:
                new_node.next = previous_node.next
                previous_node.next = new_node
                break
            counter += 1
            previous_node = previous_node.next
            current_node = current_node.next

    def list_length(self):
        current_node = self.head.next
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def remove(self, data):
        previous_node = self.head
        current_node = self.head.next

        while current_node is not None:

            if current_node.data == data:
                previous_node.next = current_node.next
                current_node.next = None
                break

            previous_node = previous_node.next
            current_node = current_node.next


list1 = [4, 9, 2, 3, 5, 7, 8, 1, 6]
li = LinkedList()
# li.append(4)
# li.append(9)
# li.append(2)
# li.append(3)
# li.append(5)
# li.print_list()
# print()
# li.prepend(7)
# li.prepend(8)
# li.prepend(1)
# li.prepend(6)
# li.print_list()
# print()
# li.insert_after(5, 13)
# li.print_list()
# print()
# li.insert_after(6, 17)
# li.print_list()
# print()
# li.insert_after(9, 1)
# li.print_list()

for num in list1:
    li.append(num)

li.print_list()
# print()
# li.insert_before(2, 11)
# li.print_list()
# print()
# li.insert_before(6, 44)
# li.print_list()
print()
# li.insert_at(0, 48)
# li.print_list()
# print()
# li.insert_at(1, 63)
# li.insert_at(8, 72)
# print(f"Total Elements: {li.list_length()}")
# li.insert_at(9, 79)
# li.print_list()
# print()
# print(f"Total Elements: {li.list_length()}")
# li.insert_at(10, 83)
# li.print_list()
# print()
# print(f"Total Elements: {li.list_length()}")
# li.print_list()

# li.remove(4)
# li.remove(6)
li.remove(2)
li.print_list()
