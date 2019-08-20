import java.util.ArrayList;
import java.util.Stack;
//输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
public class offer03_从头到尾打印链表 {

    public class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        Stack<Integer> stk1 = new Stack<Integer>();
        if(listNode == null)return list;
        while(listNode != null){
            stk1.push(listNode.val);
            listNode = listNode.next;
        }
        while(!stk1.isEmpty()){
            list.add(stk1.pop());
        }
        return list;
    }
}
