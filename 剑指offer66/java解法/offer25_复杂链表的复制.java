public class offer25_复杂链表的复制 {
    public class RandomListNode {
        int label;
        RandomListNode next = null;
        RandomListNode random = null;
        RandomListNode(int label) {
            this.label = label;
        }
    }

    public RandomListNode Clone(RandomListNode pHead){
        if(pHead == null)return null;
        // head用来实时跟踪操作
        RandomListNode head = new RandomListNode(pHead.label);
        // ans用来存储所有过程中的操作
        RandomListNode ans = head;
        if(pHead.random != null)
            head.random = new RandomListNode(pHead.random.label);
        while(pHead.next != null){
            pHead = pHead.next;
            head.next = new RandomListNode(pHead.label);
            if(pHead.random != null)
                head.next.random = new RandomListNode(pHead.random.label);
            head = head.next;
        }
        return ans;
    }

}
