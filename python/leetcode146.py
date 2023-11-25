class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        node.prev = None
        node.next = None

    def remove_head(self):
        node = self.head
        self.remove(node)
        return node

    def __str__(self):
        ret = []
        node = self.head
        while node is not None:
            ret.append("({},{})".format(node.key, node.val))
            node = node.next
        return "->".join(ret)

    def __repr__(self) -> str:
        return self.__str__()


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.cache = dict()
        self.linked_list = DoubleLinkedList()


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.linked_list.remove(node)
            self.linked_list.add(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.key = key
            self.linked_list.remove(node)
            self.linked_list.add(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.linked_list.add(node)
            self.size += 1
            if self.size > self.cap:
                head = self.linked_list.remove_head()
                del self.cache[head.key]
                self.size -= 1




lRUCache = LRUCache(10)
lRUCache.put(10, 13)
lRUCache.put(3, 17)
lRUCache.put(6, 11)
lRUCache.put(10, 5)
lRUCache.put(9, 10)
lRUCache.get(13)
lRUCache.put(2, 19)
lRUCache.get(2)
lRUCache.get(3)
print(lRUCache.linked_list)
lRUCache.put(5, 25)
lRUCache.get(8)
lRUCache.put(9, 22)
lRUCache.put(5, 5)
lRUCache.put(1, 30)
lRUCache.get(11)
lRUCache.put(9, 12)
lRUCache.get(7)
