/*
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
*/
public class offer07_斐波那契数列 {
    public int Fibonacci(int n) {
        if(n == 0)return 0;
        if(n == 1)return 1;
        int fib = 0, num1 = 0, num2 = 1;
        for(int i =2; i <= n; i++){
            fib = num1 + num2;
            num1 = num2;
            num2 = fib;
        }
        return fib;
    }
}
