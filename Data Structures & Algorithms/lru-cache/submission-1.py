
class LRUCache:

    def __init__(self, capacity: int):
        # dummy nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nex = self.right
        self.right.pre = self.left
        self.cache = {} # key->Node
        self.n = capacity

    def insert(self, node):
        p = self.right.pre
        p.nex = node
        node.nex = self.right
        node.pre = p
        self.right.pre = node

    def remove(self, node):
        p = node.pre
        n = node.nex
        p.nex = n
        n.pre = p

    def get(self, key: int) -> int:
        print("get",key,self.cache)
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache.pop(key)
            self.remove(old_node)

        new_node = Node(key,value)
        self.insert(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.n:
            old_node = self.left.nex
            print(old_node.key, old_node.value)
            self.remove(old_node)
            del self.cache[old_node.key]
        print("put",key, value, self.cache)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.nex = None
