class Node(object):
    def __init__(self, data, next=None):
        self.val = data
        self.next = next


def fanzhuan1(head):
    if head == None:
        return None
    #t用来记录原链表中下一个元素位置，next用来记录反转后的链表元素
    t, cur, next = None, head, None

    while cur:
        #t记录下一个元素
        t = cur.next
        #改变当前元素的指向方向
        cur.next = next
        #把现在的元素记录，给下一个元素作方向
        next = cur
        #移动到下一个元素
        cur = t
    return next

def fanzhuan2(head):
    if not head: return None
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    new_head = Node(0)
    tmp = new_head
    for node in arr[::-1]:
        tmp.next = Node(node)
        tmp = tmp.next

    return new_head.next


def create_listnode(arr):
    pre = Node(0)
    tmp = pre
    for i in arr:
        tmp.next = Node(i)
        tmp = tmp.next
    return pre.next

def print_listnode(head):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next


head = create_listnode(range(9))
print_listnode(head)
print_listnode(fanzhuan2(head))
# print_listnode(fanzhuan1(head))
