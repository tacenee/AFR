class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}

// 1.就地反转法
    public ListNode reverseList1(ListNode head) {
        if (head == null)
            return head;
		//dummy位置固定不变
        ListNode dummy = new ListNode(-1);
		//head是要反转的位置
        dummy.next = head;
		//命名dummy的下一个是prev，这个位置是固定不变的
        ListNode prev = dummy.next;
		//命名prev的下一个是这次要反转的位置
        ListNode pCur = prev.next;
        while (pCur != null) {
			//告诉prev你要指向的人是我前面的那个人
            prev.next = pCur.next;
			//告诉pcur你要指向的人是现在dummy前面那个人
            pCur.next = dummy.next;
			//pcur不是换了位置吗，告诉pcur你后面那个人是dummy
            dummy.next = pCur;
			//然后将现在prev现在前面的人叫pcur
            pCur = prev.next;
        }
        return dummy.next;
    }
	
	
	public Node reverse(Node node,Node prev){
		if(node.next==null){
			node.next=prev;
			return node;
		}else{
			Node re = reverse(node.next,node);
			node.next=prev;
			return re;
		}
	}
	
	public Node reverse2(Node node){
		if(node.next==null){
			return node;
		}
		Node next = node.next;
		node.next=null;
		Node re = reverse2(next);
		next.next=node;
		return re;
	}
	
	