def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val >= l2.val :
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2

def sortList(self, head: ListNode) -> ListNode:
    if not (head and head.next):
        return head
    # 초기화는 같은 위치에서 slow와 fast가 시작함.
    mid, slow, fast = None, head, head
    if fast and fast.next:
       #mid는 slow자리, slow는 한칸 앞으로, fast는 두 칸 앞으로 이동
       mid, slow, fast = slow, slow.next, fast.next.next; 
    mid.next = None

    l1 = self.sortList(head)
    l2 = self.sortList(slow)

    return mergeTwoLists(l1, l2)
