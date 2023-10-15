class listNode:
    def __init__(self, key = 0, val = 0):
        self.key, self.val = key, val
        self.prev = self.next= None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        # create double linked list
        self.left, self.right = listNode(), ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nextNode = node.prev, node.next
        prev.next = nextNode
        nextNode.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.hashmap: 
            # remove node from linked list and them add to the right
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # update, if key in hashmap
        if key in self.hashmap: 
        # remove node from linked list 
            self.remove(self.hashmap[key])
        # Either case, add add new Node to the hashmap and linked list
        self.hashmap[key] = listNode(key, value)
        self.insert(self.hashmap[key])
        # if exceed cap, remove left node
        if len(self.hashmap) > self.cap:
            lru = self.left.next
            self.remove(lru)
            # delete node from hashmap
            del self.hashmap[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)