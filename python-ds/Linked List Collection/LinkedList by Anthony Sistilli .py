# 2 simple ways to code linked lists in python
# ref: anthony sistilli

# "3" -> "7" -> "10"

# # method - 01
# class LinkedListNode:
#     def __init__(self, value, nextNode=None):
#         self.value = value
#         self.nextNode = nextNode
#
# node1 = LinkedListNode("3")
# node2 = LinkedListNode("7")
# node3 = LinkedListNode("10")
# node4 = LinkedListNode("77")
#
# node1.nextNode = node2  # node1 -> node2, "3" -> "7"
# node2.nextNode = node3  # node2 -> node3, "7" -> "10"
# node3.nextNode = node4
# # node1 -> node2 -> node3
#
# currentNode = node1
# while True:
#     print(f"{currentNode.value} ->", end=" ")
#     if currentNode.nextNode is None:
#         print("None")
#         break
#     currentNode = currentNode.nextNode


# method - 2
class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(f"{currentNode.value} ->", end=" ")
            currentNode = currentNode.nextNode
        print("None")


ll = LinkedList()
ll.printLinkedList()
ll.insert("3")
ll.printLinkedList()
ll.insert("44")
ll.printLinkedList()
ll.insert("55")
ll.printLinkedList()


