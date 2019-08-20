/*
例如，“student. a am I”。
后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
*/
public class offer44_翻转单词 {
    public String ReverseSentence(String str) {
        if("".equals(str.trim())) return str;
        String[] word = str.split(" ");
        StringBuffer sb = new StringBuffer();
        for(int i = word.length - 1; i >= 0; i--){
            sb.append(word[i] + " ");
        }
        return sb.toString().trim();
    }
}
