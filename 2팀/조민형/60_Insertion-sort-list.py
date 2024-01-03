# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        copy_head = head
        
        while copy_head:
            prev = dummy
            next_temp = copy_head.next

            while prev.next and prev.next.val < copy_head.val:
                prev = prev.next

            copy_head.next = prev.next
            prev.next = copy_head

            copy_head = next_temp

        return dummy.next

                
