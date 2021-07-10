class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_length):
        self.table_length = table_length
        self.hash_table = [None] * table_length

    def custom_hash(self, key):
        hash_key = 0
        for i in key:
            hash_key += ord(i)
            hash_key = (hash_key * ord(i)) % self.table_length
        return hash_key

    def add_key_value(self, key, value):
        hash_key = self.custom_hash(key)
        if self.hash_table[hash_key] is None:
            self.hash_table[hash_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hash_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hash_key = self.custom_hash(key)
        node = self.hash_table[hash_key]
        if node is None:
            return None
        if node.next_node:
            while node.next_node:
                if node.data.key is key:
                    return node.data.value
                node = node.next_node
        if node.data.key is key:
            return node.data.value

    def preview(self):
        print("{")
        for i, node in enumerate(self.hash_table):
            if node is not None:
                ht_string = ""
                if node.next_node:
                    while node.next_node:
                        ht_string += (
                            f"({str(node.data.key)} : {str(node.data.value)}) --> "
                        )
                        node = node.next_node
                    ht_string += (
                        f"({str(node.data.key)} : {str(node.data.value)}) --> None"
                    )
                    print(f"    [{i}] -> {ht_string}")
                else:
                    print(f"    [{i}] -> ({node.data.key} : {node.data.value})")
            else:
                print(f"    [{i}] -> ({node})")
        ht_string += "}"
        print("{")


# ht = HashTable(4)
# ht.add_key_value("hi", "hello")
# ht.add_key_value("song", "Jon Bellion")
# ht.add_key_value("odogwu", "Burna boy")
# ht.add_key_value("silanka", "Fullstack DS/ML")

# print(ht.get_value("silanka"))
# print(ht.get_value("song"))
# print(ht.get_value("songs"))
