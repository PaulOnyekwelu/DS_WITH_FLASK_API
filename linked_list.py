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
        if self.head is None:
            self.head = Node(data, self.head)
            self.last_node = self.head
        else:
            node = Node(data, self.head)
            self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next_node
        return result

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None

    def print_ll(self):
        string_ll = ""
        node = self.head
        while node:
            string_ll += f" {str(node.data)} ->"
            node = node.next_node
        string_ll += " None"
        print(string_ll)
