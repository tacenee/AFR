class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None: return
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        cur = slow.next
        #一定要把中间位置的下一个置空
        slow.next = None
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        p2 = pre
        p1 = head
        while p2:
            next1 = p1.next
            next2 = p2.next
            p1.next = p2
            p2.next = next1

            p1 = next1
            p2 = next2
        return head

