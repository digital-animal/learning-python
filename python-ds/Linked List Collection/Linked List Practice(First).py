class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        if self.head.next is None:
            self.head.next = new_node
            return

        current_node = self.head.next
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def print_list(self):
        current_node = self.head.next
        # print(current_node)
        # print(current_node.data)
        # print(current_node.next)
        # print(current_node.next.data)
        # print(current_node.next.next)
        # print(current_node.next.next.data)
        # print(current_node.next.next.next)
        # print(current_node.next.next.next.data)
        # print(current_node.next.next.next.next)
        while current_node:
            print(current_node.data, end=" => ")
            current_node = current_node.next

    def search(self, item):
        current_node = self.head.next

        while current_node is not None:
            if current_node.data == item:
                print(f"{item} found in the list")
                return True
            current_node = current_node.next
        else:
            print(f"{item} not found in the list")
            return False

    def remove(self, key):
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == key:
                previous_node.next = current_node.next
                print(f"{key} deleted from the list")
                return
            # previous_node = current_node
            previous_node = previous_node.next
            current_node = current_node.next
        print(f"{key} not present in the list")

    def insert_after(self, data, new_data):
        current_node = self.head.next
        new_node = Node(new_data)

        while current_node is not None:
            if current_node.data == data:
                new_node.next = current_node.next
                current_node.next = new_node
                print(f"{new_data} inserted after {data}")
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
                print(f"{new_data} inserted before {data}")
                break
            previous_node = previous_node.next
            current_node = current_node.next

    def insert_at(self, num, index):
        assert index <= li.list_length() , "List index out of range"
        previous_node = self.head
        current_node = self.head.next
        counter = 0

        new_node = Node(num)

        # while current_node is not None:
        while counter <= li.list_length():
            if counter == index:
                # li.insert_before(current_node.data, num)
                # print(f"{num} inserted at index {index}")
                # break

                # new_node.next = previous_node.next
                new_node.next = current_node
                previous_node.next = new_node
                print(f"{num} inserted at index {index}")
                break
            counter += 1
            previous_node = previous_node.next
            current_node = current_node.next



    def list_length(self):
        # print(self.head.data)
        # print(self.head.next)
        current_node = self.head.next
        count = 0
        while current_node is not None:
            current_node = current_node.next
            count += 1

        return count


li = LinkedList()
li.append(4)
li.append(9)
li.append(2)
li.append(3)
li.append(5)
li.print_list()
print()
li.prepend(7)
li.prepend(8)
li.print_list()
print()
# num = int(input("Enter a key to search> "))
# state = li.search(num)
# print(state)

# num = int(input("Enter a key to delete> "))
# li.remove(num)
# li.print_list()

# data = int(input("Enter the element after which you want to insert> "))
# new_data = int(input("Enter the element to insert> "))
# li.insert_after(data, new_data)
# li.print_list()

# data = int(input("Enter the element before which you want to insert> "))
# new_data = int(input("Enter the element to insert> "))
# li.insert_before(data, new_data)
# li.print_list()

print(li.list_length())


num = int(input("Enter the element to insert> "))
index = int(input("Enter the index at which you want to insert a data> "))
li.insert_at(num, index)
li.print_list()