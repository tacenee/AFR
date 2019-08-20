import java.util.ArrayList;

//题目描述
//从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
public class offer60_把二叉树打印成多行 {
	public class TreeNode {
	    int val = 0;
	    TreeNode left = null;
	    TreeNode right = null;

	    public TreeNode(int val) {
	        this.val = val;

	    }

	}
    ArrayList<ArrayList<Integer> > Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        if(pRoot == null)return result;
        ArrayList<TreeNode> nodes = new ArrayList<>();
        nodes.add(pRoot);
        func(result, nodes);
        return result;
    }
    public void func(ArrayList<ArrayList<Integer>> result, ArrayList<TreeNode> nodes){
        if(!nodes.isEmpty()){
            ArrayList<Integer> temp = new ArrayList<>();
            ArrayList<TreeNode> next = new ArrayList<>();
            for(TreeNode t : nodes){
                temp.add(t.val);
                if(t.left != null)next.add(t.left);
                if(t.right != null)next.add(t.right);
            }
            result.add(temp);
            func(result, next);
        }
    }
}
