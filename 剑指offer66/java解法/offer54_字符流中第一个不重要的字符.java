/*
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
*/
public class offer54_字符流中第一个不重要的字符 {
    //Insert one char from stringstream
    // 用来分配空间，最大空间为256; 实现单次插入；
    private char [] chars = new char[256];
    StringBuilder sb = new StringBuilder();
    public void Insert(char ch){
        chars[ch]++;
        sb.append(ch);
    }
  //return the first appearence once char in current stringstream
    public char FirstAppearingOnce(){
        char [] charArray = sb.toString().toCharArray();
        for(int i = 0; i < charArray.length; i++){
            if(this.chars[charArray[i]] == 1){
                return charArray[i];
            }
        }
        return '#';
    }
}
