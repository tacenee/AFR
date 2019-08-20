
public class offer58_是否是对称二叉树 {
	public class Solution {
		public class TreeNode {
		    int val = 0;
		    TreeNode left = null;
		    TreeNode right = null;

		    public TreeNode(int val) {
		        this.val = val;
		    }
		}
		
	    boolean isSymmetrical(TreeNode pRoot)
	    {
	        if(pRoot == null)return true;
	        return isSymmetrical(pRoot.left, pRoot.right);
	    }
	    public boolean isSymmetrical(TreeNode left, TreeNode right){
	        if(left == null && right == null)return true;
	        if(left == null || right == null)return false;
	        if(left.val == right.val)
	            return isSymmetrical(left.left, right.right)
	            		&&isSymmetrical(left.right, right.left);
	        return false;
	    }
	}
}
