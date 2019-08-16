class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            # fast = head.next

            if fast == slow:
                return True
        return False