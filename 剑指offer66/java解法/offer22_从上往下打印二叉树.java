import java.util.ArrayList;

public class offer22_从上往下打印二叉树 {
    public class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;

        }
    }

    public ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        if(root == null)return list;
        ArrayList<TreeNode> treelist = new ArrayList<TreeNode>();
        treelist.add(root);
        for(int i = 0; i < treelist.size(); i++){
            TreeNode node = treelist.get(i);
            if(node.left != null)treelist.add(node.left);
            if(node.right != null)treelist.add(node.right);
            list.add(node.val);
        }
        return list;
    }
}
