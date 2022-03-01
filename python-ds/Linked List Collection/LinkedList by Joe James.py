class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

    def to_string(self):
        return f"Node value : {str(self.data)}"


class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def add_node(self, n):
        n.set_next(self.root)
        self.root = n
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == d:
                prev_node.set_next(this_node.get_next())
            else:
                self.root = this_node.get_next()
            self.size -= 1
            return True  # data removed
        else:
            prev_node = this_node
            this_node = this_node.get_next()
        return False  # data not found

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() is None:
                return False
            else:
                this_node = this_node.get_next()

    def print_list(self):
        print("Printing list..")
        if self.root is None:
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())

    def sort(self):
        if self.size > 1:
            new_list = []
            current = self.root
            new_list.append(current)
            while current.has_next():
                new_list.append(current)
            new_list = sorted(new_list, key=lambda node: node.get_data(), reverse=True)
            new_linked_list = LinkedList()
            for node in new_list:
                new_linked_listl.add_node(node)
            return new_linked_list
        return self


def main():
    li = LinkedList()
    li.add(4)
    li.add(9)
    li.add(2)
    li.add(3)
    li.add(5)
    print(f"size = {str(li.get_size())}")
    # li.remove(9)
    # print(f"size = {str(li.get_size())}")
    # print(f"Remove 12 {li.remove(12)}")
    # print(f"size = {li.get_size()}")
    # print(f"Find 25 {li.find(25)}")
    li.print_list()
    li = li.sort()
    li.print_list()


main()
