//输入一个链表，反转链表后，输出新链表的表头。
public class offer15_反转链表 {
    public class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode ReverseList(ListNode head) {
        ListNode pre = null;
        ListNode p = null;
        if(head == null)return null;
        while(head != null){
            p = head.next;
            head.next = pre;
            pre = head;
            head = p;
        }
        return pre;
    }
}
