from LLFG import Node, LinkedList


class NewNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)


def merge_list(li1, li2, li3):
    current_of_first = li1.head.next
    current_of_second = li2.head.next

    while True:
        if current_of_first is None:
            li3.insert_end(current_of_second)
            break

        if current_of_second is None:
            li3.insert_end(current_of_first)
            break

        if current_of_first.data <= current_of_second.data:
            temp_next = current_of_first.next
            current_of_first.next = None
            li3.insert_end(current_of_first)
            current_of_first = temp_next

        elif current_of_first.data > current_of_second.data:
            temp_next = current_of_second.next
            current_of_second.next = None
            li3.insert_end(current_of_second)
            current_of_second = temp_next


li1 = LinkedList()

first_node = NewNode(1)
second_node = NewNode(2)
third_node = NewNode(3)
fourth_node = NewNode(3)
fifth_node = NewNode(5)

li1.insert_end(first_node)
li1.insert_end(second_node)
li1.insert_end(third_node)
li1.insert_end(fourth_node)
li1.insert_end(fifth_node)

li2 = LinkedList()

node1 = NewNode(2)
node2 = NewNode(5)
node3 = NewNode(7)
node4 = NewNode(8)
node5 = NewNode(9)
node6 = NewNode(17)
node7 = NewNode(19)

li2.insert_end(node1)
li2.insert_end(node2)
li2.insert_end(node3)
li2.insert_end(node4)
li2.insert_end(node5)
li2.insert_end(node6)
li2.insert_end(node7)

print("===== Before Merging =====", end=" ")
print()
print("# List 1:", end=" ")
li1.print_list()
print()
print("# List 2:", end=" ")
li2.print_list()
print()
print()

li3 = LinkedList()
merge_list(li1, li2, li3)

print("===== After Merging =====")
print("# Combined List: ", end=" ")


li3.print_list()
