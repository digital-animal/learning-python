from LLFG import Node, LinkedList


class NewNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)


def swap_next(li, prev_node, current_node, next_node):
    # before: 4 => 9 => 2 => 3 => 5 => 7 => 8 => 1 => 6 => 0 => None
    # after: 0 => 1 => 2 => 3 => 4 => 5 => 6 => 7 => 8 => 9 => None

    current_node.next = next_node.next
    next_node.next = current_node
    prev_node.next = next_node


def bubble_sort(li):
    iteration_count = 0

    # # for debugging
    # count_inner = 0
    # count_outer = 0

    while True:
        if iteration_count == li.list_length() - 1:
            break
        previous_node = li.head
        current_node = previous_node.next
        next_node = current_node.next


        while True:
            if next_node is None:
                break
            if current_node.data > next_node.data:
                swap_next(li, previous_node, current_node, next_node)

            previous_node = current_node
            current_node = next_node
            next_node = next_node.next

            # # # for debugging
            # print(f"# # Inner Loop Execution: {count_inner} # #")
            # count_inner += 1

        iteration_count += 1

        # # for debugging
        # print(f"# # Outer Loop Count: {count_outer} # #")
        # count_outer += 1


li = LinkedList()

first_node = NewNode(4)
second_node = NewNode(9)
third_node = NewNode(2)
fourth_node = NewNode(3)
fifth_node = NewNode(5)
sixth_node = NewNode(7)
seventh_node = NewNode(8)
eighth_node = NewNode(1)
ninth_node = NewNode(6)
tenth_node = NewNode(0)

li.insert_end(first_node)
li.insert_end(second_node)
li.insert_end(third_node)
li.insert_end(fourth_node)
li.insert_end(fifth_node)
li.insert_end(sixth_node)
li.insert_end(seventh_node)
li.insert_end(eighth_node)
li.insert_end(ninth_node)
li.insert_end(tenth_node)

print("# Before Sorting:", end=" ")
li.print_list()
print()
# swap_next(li, first_node, second_node, third_node)
# li.print_list()

bubble_sort(li)
print("# After Sorting:", end=" ")
li.print_list()
