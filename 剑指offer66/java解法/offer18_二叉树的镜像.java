public class offer18_二叉树的镜像 {
    public class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;

        }
    }

    public void Mirror(TreeNode root) {
        if(root == null)return;
        if(root.left != null || root.right != null){
            TreeNode temp = root.right;
            root.right = root.left;
            root.left = temp;
            Mirror(root.left);
            Mirror(root.right);
        }
    }
}
