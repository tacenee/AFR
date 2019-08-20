/*
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
*/
public class offer10_矩形覆盖 {
    public int RectCover(int target) {
        int temp0 = 1;
        int temp1 = 1;
        int num = 0;
        if(target == 1)
            return temp1;
        for(int i = 2; i <= target; i++){
            num = temp0 + temp1;
            temp0 = temp1;
            temp1 = num;
        }
        return num;
    }
}
