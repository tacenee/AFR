class BinTree{
	int data;
	BinTree left;
	BinTree right;
	
	public BinTree(int c) {  
        date = c;  
    }  

//前序非递归
public static preOder(BinTree b){
	Stack<BinTree> s = new Stack<BinTree>();
	while(b!=null||!s.isEmpty){
		while(b!=null){
			System.out.print(b.date+" ");
			s.push(b);
			b=b.left;		
		}
		if(!s.isEmpty){
			b=s.pop();
			b=b.right;
		}
	}
}

//中序非递归
public static inOder(BinTree b){
	Stack<BinTree> s = new Stack<BinTree>();
while(b!=null||!s.isEmpty){
		while(b!=null){			
			s.push(b);
			b=b.left;		
		}
		if(!s.isEmpty){
			b=s.pop();
			System.out.print(b.data+" ");
			b=b.right;
		}
	}
}

public static postOder(BinTree b){
	Stack<BinTree> s = new Stack<BinTree>();
	Stack<Integer> ss = new Stack<Integer>();
	Integer i= 1;
	while(b!=null||!s.isEmpty){
		while(b!=null){			
			s.push(b);
			ss.push(0);
			b=b.left;		
		}
		while(!s.isEmpty&&ss.peak().equal(i)){
			System.out.print(s.pop().date+" ");
			ss.pop();
		}
		if(!s.isEmpty){
			ss.pop();
			ss.push(1);		
			b=s.peak();
			b=b.right;
		}
	}
}
}