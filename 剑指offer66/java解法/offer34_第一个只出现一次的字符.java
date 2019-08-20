public class offer34_第一个只出现一次的字符 {
    public int FirstNotRepeatingChar(String str) {
        int n = str.length();
        if(n == 0)return -1;
        int i = 0;
        while(i < n){
            int index1 = str.indexOf(str.charAt(i));
            int index2 = str.lastIndexOf(str.charAt(i));
            if(index1 == index2)return index1;
            i++;
        }
        return -1;
    }
}
