//题目描述
//给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
public class offer55_链表中环的入口 {
	 public class ListNode {
		    int val;
		    ListNode next = null;

		    ListNode(int val) {
		        this.val = val;
		    }
		}
	 
     public ListNode EntryNodeOfLoop(ListNode pHead)
     {
         if(pHead == null || pHead.next == null || pHead.next.next == null)
             return null;
         ListNode head1 = pHead.next;
         ListNode head2 = pHead.next.next;
         while (head2 != head1){
             if(head2.next != null || head2.next.next != null){
                 head1 = head1.next;
                 head2 = head2.next.next;
             }else {
                 return null;
             }
         }
         head2 = pHead;
         while (head1 != head2){
             head1 = head1.next;
             head2 = head2.next;
         }
         return head2;
     }
}
