class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            return
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
        if self.head is None:
            return self.insert_beginning(data)
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next_node
        return result

    def print_ll(self):
        node = self.head
        ll_string = ""
        while node:
            ll_string += f" {node.data} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)


linked_list = LinkedList()
linked_list.insert_beginning("hello")
linked_list.insert_end("the end!")
linked_list.insert_end("finnesse!")
linked_list.insert_beginning("Hi")
linked_list.print_ll()
print(linked_list.to_list())
