/**
*快排算法
*快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，
*其中一部分记录的关键字均比另一部分的关键字小，
*则可分别对这两部分记录继续进行排序，以达到整个序列有序。
*/

public class KuaiPai {

		/**
	     * 
	     * @param numbers 带排序数组
	     * @param low  开始位置
	     * @param high 结束位置
	     */
	  public static void quickSort(int[] numbers,int low,int high)
	    {
	       int i = low;
	       int j = high;
//	       int povit = numbers[(low+high)/2];
	       int povit = numbers[i];
	       while(i<j) {
		       while(numbers[i]<povit) {
		    	   i++;
		       }
		       while(numbers[j]>povit) {
		    	   j--;
		       }
		       if(i<=j) {
		       int temp = numbers[i];
		       numbers[i]=numbers[j];
		       numbers[j]=temp;
		       i++;
		       j--;
		       }
	       }
	       if(j>low) {
	       quickSort(numbers,low,j);
	       }
	       if(i<high) {
	       quickSort(numbers,i,high);
	       }
	    }
	  
	public static void main(String[] args) {
		int[] numbers= {13,12,34,54,67,37,22,1,99};
		quickSort(numbers,0,8);

		for(int a:numbers)
		    System.out.print(a+" ");
	}
}
