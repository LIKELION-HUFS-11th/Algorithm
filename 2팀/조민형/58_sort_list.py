def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 연결시킬 두 연결리스트가 있을 때만 작동
    if l1 and l2:
        #l1이 ㅣ2보다 크거나 같을 경우 -> 원래는 왼쪽에 있는 것이 더 작아야 하기 때문에 자리를 바꿔줌
        if l1.val >= l2.val :
            l1, l2 = l2, l1
        # l1와 l2의 자리를 바꾸고 l1의 다음 부분부터 재귀적으로 호출해 다시 비교하고 자리 바꾸기
        l1.next = self.mergeTwoLists(l1.next, l2)
    # 마지막에 남은 연결리스트를 전부 연결시킴
    return l1 or l2

def sortList(self, head: ListNode) -> ListNode:
    if not (head and head.next):
        return head
    # 초기화는 같은 위치에서 slow와 fast가 시작함.
    mid, slow, fast = None, head, head
    if fast and fast.next:
       #mid는 slow자리, slow는 한칸 앞으로, fast는 두 칸 앞으로 이동
       mid, slow, fast = slow, slow.next, fast.next.next; 
    #mid까지 이어져 있는 연결리스트의 다음을 끊어 분할시킴
    mid.next = None

    # head는 가장 처음이고, mid가 있는 곳까지의 연결 리스트에서 다시 분할
    l1 = self.sortList(head)
    # mid 다음부터 끝까지 있는 연결 리스트를 다시 분할
    l2 = self.sortList(slow)

    # 계속해서 쪼갠 것들을 다시 합치는 작업
    return self.mergeTwoLists(l1, l2)
