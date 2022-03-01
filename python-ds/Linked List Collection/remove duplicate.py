from LLFG import Node, LinkedList


class NewNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)


def remove_duplicate(li):
    current_node = li.head.next
    next_node = current_node.next

    while True:
        if next_node is None:
            break
        if current_node.data == next_node.data:
            current_node.next = next_node.next
            next_node.next = None

        current_node = next_node
        next_node = next_node.next


li = LinkedList()

first_node = NewNode(1)
second_node = NewNode(2)
third_node = NewNode(3)
fourth_node = NewNode(3)
fifth_node = NewNode(5)

li.insert_end(first_node)
li.insert_end(second_node)
li.insert_end(third_node)
li.insert_end(fourth_node)
li.insert_end(fifth_node)

print("# Before:", end=" ")
li.print_list()
print()
remove_duplicate(li)
print("# After Removing Duplicates:", end=" ")
li.print_list()
