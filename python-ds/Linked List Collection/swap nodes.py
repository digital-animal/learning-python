from LLFG import Node, LinkedList


class NewNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)


def swap_node(li, first_data, second_data):
    # before: 4 => 9 => 2 => 3 => 5 => None
    # swapped: 4 => 3 => 2 => 9 => 5 => None
    # 4=>previous_of_first || 9=>first
    # 2=>previous_of_second || 3=>second

    previous_node = li.head
    current_node = li.head.next

    previous_of_first = None
    previous_of_second = None

    while current_node is not None:
        if current_node.data == first_data:
            previous_of_first = previous_node
            first = current_node
        elif current_node.data == second_data:
            previous_of_second = previous_node
            second = current_node

        previous_node = previous_node.next
        current_node = current_node.next

    previous_of_first.next = second
    temp = second.next
    second.next = first.next
    previous_of_second.next = first
    # first.next = second.next # wrong..second of next was changed before
    first.next = temp


if __name__ == "__main__":
    li = LinkedList()

    first_node = NewNode(4)
    second_node = NewNode(9)
    third_node = NewNode(2)
    fourth_node = NewNode(3)
    fifth_node = NewNode(5)
    sixth_node = NewNode(7)
    seventh_node = NewNode(8)

    li.insert_end(first_node)
    li.insert_end(second_node)
    li.insert_end(third_node)
    li.insert_end(fourth_node)
    li.insert_end(fifth_node)
    li.insert_end(sixth_node)
    li.insert_end(seventh_node)

    print("# Before Swapping:", end=" ")
    li.print_list()
    swap_node(li, 9, 7)
    print()
    print("# After Swapping:", end=" ")
    li.print_list()
