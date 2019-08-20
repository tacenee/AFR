//请实现一个函数，把字符串中的每个空格替换成"%20"。
//例如输入“We are happy.”，则输出“We%20are%20happy.”
public class offer02_替换空格 {
    public String replaceSpace(StringBuffer str) {
        int oldLength = str.length();
        int newLength = oldLength;
        for(int i = 0; i < oldLength; i++){
            if(str.charAt(i) == ' '){
                newLength +=2;
            }
        }
        str.setLength(newLength);
        int i = oldLength - 1, j = newLength - 1;
        while( i >= 0){
            if(str.charAt(i) == ' '){
                str.setCharAt(j--, '0');
                str.setCharAt(j--, '2');
                str.setCharAt(j--, '%');
                i--;
            }else{
                str.setCharAt(j--, str.charAt(i--));
            }
        }
        return str.toString();
    }
}
