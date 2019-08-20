/**
*先序
*/

public void preorder(Node p){
	if(isEmpty){
		return;
	}
	if(p!=null){
		System.out.print(p.getDate +" ");
		preorder(p.getLChildNode);
		preorder(p.getRChildNode);
	}
	
}

/**
*中序
*/

public void inorder(Node p){
	if(isEmpty){
		return;
	}
	if(p!=null){		
		inorder(p.getLChildNode);
		System.out.print(p.getDate +" ");
		inorder(p.getRChildNode);
	}
	
}
/**
*后序
*/
public void postorder(Node p){
	if(isEmpty){
		return;
	}
	if(p!=null){		
		postorder(p.getLChildNode);		
		postorder(p.getRChildNode);
		System.out.print(p.getDate +" ");
	}
	
}