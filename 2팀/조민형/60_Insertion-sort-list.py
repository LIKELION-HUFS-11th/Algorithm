# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 아무것도 안들어왔을 때
        if not head:
            return head
        
        # 헤드쪽에 더미노드 생성
        dummy = ListNode(0)
        #위치 옮겨가면서 삽입정렬 생성할 인덱스용도
        copy_head = head
        
        # copy_head가 참일 동안 = next가 None일 때까지
        while copy_head:
            # 더미노드 복사
            prev = dummy
            # 다음 노드 를 next_temp에 복사(나중에 옆으로 옮길 용도. 중간에 next가 바뀌기 때문)
            next_temp = copy_head.next

            # 다음 노드가 있고 노드가 멈출 위치 설정(다음 노드보다 작을때)
            while prev.next and prev.next.val < copy_head.val:
                # 해당 삽입할 위치까지 계속해서 이동
                prev = prev.next

            # 원래 copy_head의 next에 들어갈 자리에 prev.next를 연결 
            copy_head.next = prev.next
            # prev의 다음 노드는 copy_head로 변경해서
            # prev -> copy_head -> prev.next 이 순서대로 되도록 연결
            prev.next = copy_head

            # copy_head를 원래 저장해놨던 다음 노드로 이동
            copy_head = next_temp

        # 더미노드 다음 노드부터 진짜 연결리스트이므로 dummy.next를 리턴
        return dummy.next

                
