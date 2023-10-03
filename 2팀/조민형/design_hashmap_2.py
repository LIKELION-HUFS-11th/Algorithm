class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        else:
            nodes = self.table[index]
            while nodes:
                if nodes.key == key:
                    nodes.value = value
                    return
                if nodes.next is None:
                    break
                nodes = nodes.next
            nodes.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        else:
            nodes = self.table[index]
            while nodes:
                if nodes.key == key:
                    return nodes.value
                nodes = nodes.next
            return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        else:
            nodes = self.table[index]
            if nodes.key == key:
                self.table[index] = ListNode(
                ) if nodes.next is None else nodes.next
                return
        prevnodes = nodes
        while nodes:
            if nodes.key == key:
                prevnodes.next = nodes.next
                return
            prevnodes, nodes = nodes, nodes.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
