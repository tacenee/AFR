/*
 题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 
数值为0或者字符串不是一个合法的数值则返回0。
 */
public class offer49_字符串转整数 {
    public int StrToInt(String str) {
        if(str.equals(" ") || str.length() == 0)return 0;
        char[] charArr = str.toCharArray();
        int fuhao = 0;
        if(charArr[0] == '-')fuhao = 1;
        int sum = 0;
        for(int i = fuhao; i < charArr.length; i++){
            if(charArr[i] == '+')continue;
            if(charArr[i] < 48 || charArr[i] > 57)return 0;
            sum = sum*10 + charArr[i] - 48;
        }
        return fuhao == 0 ? sum : -1 * sum;
    }
}
