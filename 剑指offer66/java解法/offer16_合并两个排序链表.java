//输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
public class offer16_合并两个排序链表 {
    public class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ListNode Merge(ListNode list1,ListNode list2) {
        if(list1 == null)return list2;
        if(list2 == null)return list1;
        ListNode newlist = new ListNode(-1);
        ListNode node = newlist;
        while(list1 != null && list2 != null){
            if(list1.val <= list2.val){
                node.next = list1;
                node = node.next;
                list1 = list1.next;
            }else{
                node.next = list2;
                node = node.next;
                list2 = list2.next;
            }
        }
        if(list1 != null)node.next = list1;
        if(list2 != null)node.next = list2;
        return newlist.next;
    }
}
