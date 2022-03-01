# # ==========================================================
# # Part 5 - Brain Teaser (Problem Solving with linked lists)
# # ==========================================================
# # 01-02 detecting a cycle between the nodes of a singly linked list

from LLFG import Node, LinkedList


class NewNode(Node):
    def __init__(self, data):
        # super().__init__(data)
        Node.__init__(self, data)

        self.is_visited = False


def detect_cycle(li):
    current_node = li.head
    current_node.is_visited = True

    while True:
        if current_node.next.is_visited is True:
            current_node.next = None
            break
        current_node = current_node.next
        current_node.is_visited = True


li = LinkedList()

first_node = NewNode(10)
second_node = NewNode(20)
third_node = NewNode(30)
fourth_node = NewNode(40)

li.insert_end(first_node)
li.insert_end(second_node)
li.insert_end(third_node)
li.insert_end(fourth_node)

fourth_node.next = third_node
detect_cycle(li)
li.print_list()
