# ListNode 클래스는 연결 리스트
# val은 노드의 값, next는 다음 노드에 대한 참조

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 결과 연결 리스트의 루트와 현재 결과 노드를 초기화
        root = result = ListNode(None)

        # 최소 힙(heap)을 초기화
        # 힙은 (노드 값, 리스트 인덱스, 노드) 튜플
        heap = []

        # 주어진 k개의 연결 리스트를 반복
        for i in range(len(lists)):
            # 현재 연결 리스트가 비어 있지 않으면 첫 번째 노드를 최소 힙에 추가
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                print(heap)

        # 최소 힙에서 노드를 빼내면서 결과 연결 리스트를 구성
        while heap:
            # 최소 힙에서 가장 작은 노드를 빼내기
            node = heapq.heappop(heap)

            # 노드가 속한 리스트의 인덱스와 노드를 가져오기
            index = node[1]
            result.next = node[2]

            # 결과 노드를 다음 노드로 업데이트하고, 다음 노드가 있다면 최소 힙에 추가
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, index, result.next))

        # 결과 연결 리스트의 시작인 더미 노드(root)의 다음 노드를 반환
        return root.next
