//题目描述
//地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次
//只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数
//位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因
//为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
//请问该机器人能够达到多少个格子？
public class offer66_机器人的运动范围 {
    public int movingCount(int threshold, int rows, int cols)
    {
        int[][] flag = new int[rows][cols];
        return mc(threshold, rows, cols, 0, 0, flag);
    }
    public int mc(int threshold, int rows, int cols, int i, int j, int[][] flag){
        if(i < 0 || i >= rows || j < 0 || j >= cols || bitSum(i) + bitSum(j) >threshold || flag[i][j] == 1)
            return 0;
        flag[i][j] = 1;
        return mc(threshold, rows, cols, i+1, j, flag)+mc(threshold, rows, cols, i-1, j, flag)
                +mc(threshold, rows, cols, i, j+1, flag)+mc(threshold, rows, cols, i, j-1, flag)+1;
    }
    public int bitSum(int n){
        if(n == 0)return 0;
        int sum = 0;
        while (n != 0){
            sum += n%10;
            n = n/10;
        }
        return sum;
    }
}
