/*
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
*/
public class offer08_跳台阶 {
    public int JumpFloor(int target) {
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
