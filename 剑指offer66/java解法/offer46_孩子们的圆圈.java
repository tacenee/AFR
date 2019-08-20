/*
让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且
不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到
剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额
有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
*/
public class offer46_孩子们的圆圈 {
    public int LastRemaining_Solution(int n, int m) {
        if(n == 0 || m == 0)return -1;
        int count = n;
        int i = -1, step = 0;
        int[] list = new int[n];
        while(count > 0){
            i++;
            i = i % n;
            if(list[i] == -1)continue;
            step++;
            if(step == m){
                list[i] = -1;
                step = 0;
                count--;
            }
        }
        return i;
    }
}
