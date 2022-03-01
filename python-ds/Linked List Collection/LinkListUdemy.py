class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is: ")
            p = self.start
            while p is not None:
                print(f"{p.info}", end=" ")
                p = p.link()
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print(f"Number of nodes in the list = {n}")
        print()

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(f"{x} is at position {position}")
                print()
                return True
            position += 1
        else:
            print(f"{x} not found in the list.")
            print()
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes> "))
        if n == 0:
            return
        for i in range(n):
            data = int(input(f"Enter number {i+1}> "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(f"{x} is not in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        # if list is empty
        if self.start is None:
            print("List is empty")
            return

        # x is in first node, new node is to be inserted before first node
        if x == self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        # find reference to predecessor of node containing x
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(f"{x} is not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        p = self.start
        i = 1
        while i < (k - 1) and p is not None:
            p = p.link
            i += 1
        if p is None:
            print(f"You can insert only upto position {i}")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, x):
        if self.start is None:
            print("List is empty")
            return
        # deletion of first node
        if self.start.info == x:
            self.start = self.start.link
            return

        # deletion in between or at the end
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                 break
            p = p.link

        if p.link is None:
            print(f"Element {x} not in the list")
        else:
            p.link = p.link.link

    def delete_first_node(self):
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return
        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sort_ex_data(self):
        pass

    def bubble_sort_ex_links(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort(self):
        pass

    def _merge_sort_rec(self, list_start):
        pass

    def _divide_list(self, p):
        pass


# ======================================================
li = SingleLinkedList()
li.create_list()

while True:
    print("=================================================")
    print("1.Display list")
    print("2.Count the number of nodes")
    print("3.Search for an element")
    print("4.Insert in empty list/Insert in the beginning of the list")
    print("5.Insert a node at the end of the list")
    print("6.Insert a node after a specific node")
    print("7.Insert a node before a specific node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10.Delete last node")
    print("11.Delete any node")
    print("12.Reverse the list")
    print("13.Bubble sort by exchanging data")
    print("14.Bubble sort by exchanging links")
    print("15.Merge Sort")
    print("16.Insert Cycle")
    print("17.Delete Cycle")
    print("18.Remove Cycle")
    print("19.Quit")

    option = int(input("Enter your choice: "))
    if option == 1:
        li.display_list()
    elif option == 2:
        li.count_nodes()
    elif option == 3:
        data = int(input("Enter the element to be searched> "))
        li.search(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted> "))
        li.insert_in_beginning(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted> "))
        li.insert_at_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted> "))
        x = int(input("Enter the element after which to insert> "))
        li.insert_after(data, x)
    elif option == 7:
        data = int(input("Enter the element to be inserted> "))
        x = int(input("Enter the element before which to insert> "))
        li.insert_at_position(data, x)
    elif option == 8:
        data = int(input("Enter the element to be inserted> "))
        k = int(input("Enter the position at which to insert> "))
        li.insert_at_position(data, k)
    elif option == 9:
        li.delete_first_node()
    elif option == 10:
        li.delete_last_node()
    elif option == 11:
        data = int(input("Enter the element to be deleted> "))
        li.delete_node(data)
    elif option == 12:
        li.reverse_list()
    elif option == 13:
        li.bubble_sort_ex_data()
    elif option == 14:
        li.bubble_sort_ex_links()
    elif option == 15:
        li.merge_sort()
    elif option == 16:
        data = int(input("Enter the element at which the cycle has to be inserted> "))
        li.insert_cycle(data)
    elif option == 17:
        if li.has_cycle():
            print("List has a cycle.")
        else:
            print("List does not have a cycle")
    elif option == 18:
        li.remove_cycle()
    elif option == 19:
        break
    else:
        print("Wrong Option")
