public class offer36_两个链表的第一个公共节点 {

    public class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if(pHead1 == null || pHead2 == null)return null;
        ListNode head1 = pHead1;
        while(head1 != null){
            ListNode head2 = pHead2;
            while(head2 != null){
                if(head2 == head1)return head1;
                head2 = head2.next;
            }
            head1= head1.next;
        }
        return null;
    }
}
