class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def sortList(head: ListNode) -> ListNode:
    if not head or not head.next: return head
    #暂时还没搞懂这里为什么要head的next，用head就会超出递归深度
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    mid = slow.next
    slow.next = None
    p1, p2 = sortList(mid), sortList(head)
    h = res = ListNode(0)
    while p1 and p2:
        if p1.val < p2.val:
            h.next, p1 = p1, p1.next
        else:
            h.next, p2 = p2, p2.next
        h = h.next
    h.next = p1 if p1 else p2
    return res.next

