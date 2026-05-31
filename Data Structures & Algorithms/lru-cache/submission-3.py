
class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, size):
        self.cache = {}
        self.key_to_node = {}
        self.size = size

        start_node = Node(None)
        end_node = Node(None)
        start_node.next = end_node
        end_node.prev = start_node
        self.start = start_node
        self.end = end_node

    
    def put(self, key, value):
        if key not in self.key_to_node:
            if len(self.key_to_node.keys()) == self.size:
                self.remove_lru()
            node = Node(key)
            self.key_to_node[key] = node
            self.insert_node_to_front(node)

        self.cache[key] = value
        self.move_to_front(self.key_to_node[key])

    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.move_to_front(self.key_to_node[key])
        return self.cache[key]

    def insert_node_to_front(self, node):
        cur_first = self.start.next
        cur_first.prev = node
        node.next = cur_first
        node.prev = self.start
        self.start.next = node

    def move_to_front(self, node):
        # join node.prev and node.next
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        cur_head = self.start.next
        self.start.next = node
        node.prev = self.start
        node.next = cur_head
        cur_head.prev = node

    # remove end
    def remove_lru(self):
        node_to_remove = self.end.prev
        print(f"removing {node_to_remove.key}, cache:{self.cache}")
        node_to_remove.prev.next = self.end
        self.end.prev = node_to_remove.prev
        self.cache.pop(node_to_remove.key)
        self.key_to_node.pop(node_to_remove.key)
