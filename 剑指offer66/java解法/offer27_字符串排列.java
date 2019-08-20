/*
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
*/
import java.util.ArrayList;
import java.util.Collections;

public class offer27_字符串排列 {
    public ArrayList<String> Permutation(String str) {
        ArrayList<String> res = new ArrayList<String>();
        if(str.length() == 0)return res;
        dealer(res, 0, str.toCharArray());
        Collections.sort(res);
        return res;
    }
    private void dealer(ArrayList<String> res, int j, char[] s){
        if(j == s.length - 1)
            res.add(new String(s));
        for(int i = j; i < s.length; i++){
            if(i ==j || s[i] != s[j]){
                swap(s, i, j);
                dealer(res, j + 1, s);
                swap(s, i, j);
            }
        }
    }
    private void swap(char[] s, int i, int j){
        char sig = s[i];
        s[i] = s[j];
        s[j] = sig;
    }
}
