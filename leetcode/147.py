class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSortList(head: ListNode) -> ListNode:
    # 因为有小于0的元素存在，所以初始化的时候 定为负无穷
    dummy = ListNode(float('-inf'))
    pre = dummy
    tail = dummy
    cur = head
    while cur:
        if tail.val < cur.val:
            tail.next = cur
            tail = cur
            cur = cur.next
        else:
            # 暂时不能确定tail的位置，但是可以确定tail下一个指向的位置
            tmp = cur.next
            tail.next = tmp
            # 找到要插入的位置
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            #插入这个元素，然后从下一个元素重新开始
            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = tmp
    return dummy.next
