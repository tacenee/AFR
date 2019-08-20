//题目描述
//在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
//重复的结点不保留，返回链表头指针。 
//例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
public class offer56_删除链表中重复的结点 {
	 public class ListNode {
		    int val;
		    ListNode next = null;

		    ListNode(int val) {
		        this.val = val;
		    }
		}
	 
    public ListNode deleteDuplication(ListNode pHead){
        ListNode list = new ListNode(1);
        list.next = pHead;
        ListNode temp = pHead;
        ListNode res = list;

        while(temp != null){
            if(temp.next != null && temp.val == temp.next.val){
                while (temp.next != null && temp.val == temp.next.val){
                    temp = temp.next;
                }
                temp = temp.next;
                list.next = temp;
            }else{
                temp = temp.next;
                list = list.next;
            }
        }
        return res.next;
    }
}
