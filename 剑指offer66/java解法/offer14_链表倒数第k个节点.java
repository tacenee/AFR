/*
题目描述
输入一个链表，输出该链表中倒数第k个结点。
*/
public class offer14_链表倒数第k个节点 {
    public class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

     public  ListNode FindKthToTail(ListNode head, int k)
    {
        if(head == null || k == 0)
        {
            return null;
        }

        ListNode ahead = head;
        ListNode behind = null;

        for (int i = 0; i < k - 1; i++)
        {
            if(ahead.next != null)
            {
                ahead = ahead.next;
            }
            else
            {
                return null;
            }
        }

        behind = head;

        while (ahead.next != null)
        {
            ahead = ahead.next;
            behind = behind.next;
        }

        return behind;
    }

}
