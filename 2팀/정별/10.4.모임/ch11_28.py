import collections

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

        #해시함수 mod로 인덱스값 지정
        index = key % self.size

        # 테이블이 비어있을 경우 해시값 할당
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 테이블이 차있을 경우(해시 충돌) 연결리스트 설정
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key %self.size

        # 값이 없을 때
        if self.table[index].value is None:
            return
        
        #값이 있을 때(인덱스 첫번째 노드일 때)
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next

        # 연결리스트 삭제
        prev  = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

hashMap = MyHashMap();

hashMap.put(1, 2);
print(hashMap.get(3));


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)