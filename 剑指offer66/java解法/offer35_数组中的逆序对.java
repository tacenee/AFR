/*
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
*/
public class offer35_数组中的逆序对 {
    public int InversePairs(int [] array) {
        if(array==null||array.length==0){
            return 0;
        }
        int[] copy = new int[array.length];
        for(int i=0;i<array.length;i++){
            copy[i] = array[i];
        }
        int count = InversePairsCore(array,copy,0,array.length-1);//数值过大求余
        return count;
    }
    private int InversePairsCore(int[] array,int[] copy,int low,int high)
    {
        if(low==high)return 0;
        int mid = (low+high)>>1;
        int leftCount = InversePairsCore(array,copy,low,mid)%1000000007;
        int rightCount = InversePairsCore(array,copy,mid+1,high)%1000000007;
        int count = 0;//计数--逆序对的数目
        int i=mid;//i初始化为前半段最后一个数字的下标
        int j=high;//j初始化为后半段最后一个数字的下标
		//locCopy只影响当前这一段的排序，从最高为high减去总长度
        int locCopy = high;//辅助数组复制的数组的最后一个数字的下标
        while(i>=low&&j>mid){
			//归并，将大的往后排，直到有一方排完了
            if(array[i]>array[j]){
				//i是小于中位数的，所以中位数之前的比后面大，都属于逆序，都需要加
				//j的位置到中位数是后半段所有比现在i小的数
                count += j-mid;
				//然后此时再从前半段找有没有比j现在最大的数大的
                copy[locCopy--] = array[i--];
                if(count>=1000000007)//数值过大求余
                {
                    count%=1000000007;
                }
            }else{
				//前半段没有彼此是j大的，所以找一个比j小的数跟i比大小
                copy[locCopy--] = array[j--];
            }
        }
		//另一方没有排完的，肯定都是小的，直接向前添加
        for(;i>=low;i--){
            copy[locCopy--]=array[i];
        }
        for(;j>mid;j--){
            copy[locCopy--]=array[j];
        }
        for(int s=low;s<=high;s++){
            array[s] = copy[s];
        }
        return (leftCount+rightCount+count)%1000000007;
    }
}
