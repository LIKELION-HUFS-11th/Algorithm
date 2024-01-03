# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #새로운 결과 담아줄 리스트 선언
        newlist = []
        #새 리스트에 모든 연결리스트의 값 넣어주기
        while head :
            newlist.append(head.val)
            head = head.next
        
        #파이썬 내장함수 sort로 정렬
        newlist.sort()
        
        #옮겨갈 헤드용이랑 나중에 리턴할 헤드 선언
        head = ListNode(0)
        copy_head = head

        #정렬된 리스트를 돌면서 순서대로 연결리스트 연결시키기
        for val in newlist:
            head.next = ListNode(val)
            head = head.next
        
        #리턴용 헤드(더미노드) 다믕부터 리턴
        return copy_head.next
            
            
             
