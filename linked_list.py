class Node:
    """a class for instantiating nodes"""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """for keeping track of node head"""

    def __init__(self):
        self.head = None
        self.last_node = None

    def insert_beginning(self, data):
        node = Node(data, self.head)
        if self.last_node == None:
            self.last_node = self.head
        self.head = node

    def print_ll(self):
        string_ll = ""
        node = self.head
        while node:
            string_ll += f" {str(node.data)} ->"
            node = node.next_node
        string_ll += " None"
        print(string_ll)


linked_list = LinkedList()

# inserting node
linked_list.insert_beginning("I am getting it")
linked_list.insert_beginning("singly linked list is making sense")
linked_list.insert_beginning("Thank God for understanding")

linked_list.print_ll()
