/*
大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4)
*/
public class offer45_扑克牌的顺子 {
    public boolean isContinuous(int [] numbers) {
        if(numbers.length == 0)return false;
        int min = 14, max = -1;
        int[] d = new int[14];
        for(int i = 0; i < 5; i++){
            if(numbers[i] == 0)continue;
            d[numbers[i]]++;
            if(d[numbers[i]] > 1)return false;
            if(numbers[i] > max) max = numbers[i];
            if(numbers[i] < min) min = numbers[i];
            if(max - min > 4)return false;
        }
        return true;
    }
}
