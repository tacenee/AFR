/*
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
*/
public class offer23_二叉搜索树的后序遍历 {
    public boolean VerifySquenceOfBST(int [] sequence) {
        if(sequence.length == 0)
            return false;
        return vf(sequence, 0, sequence.length - 1);
    }
    private boolean vf(int [] s, int start, int root){
        if(start >= root)return true;
        int i = root;
        while(start < i && s[i-1] > s[root]) i--;
        for(int j = start; j < i; j++){
            if(s[j] > s[root])return false;
        }
        return vf(s, start, i - 1) && vf(s, i, root - 1);
    }
}
