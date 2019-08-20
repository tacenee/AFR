/**
*堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
*堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
*即子结点的键值或索引总是小于（或者大于）它的父节点。
*
 * 
 * @author Tacenee
 *
 */
public class DuiPai {

    static int left(int i) {
        return 2*i + 1;
    }
    static int right(int i) {
        return 2*i + 2;
    }
    /**
     * 
     * @param a 数组a
     * @param i 第i个结点
     * @param heapSize heapSize是数组种实际要排序的元素的长度
     */
    static void maxHeapfy(int []a,int i,int heapSize) { 
        int left = left(i);   
        int right = right(i);   
        int parent = i;
        //判断是否还有子结点
        if(left < heapSize && a[left] > a[parent]) {   //
            parent = left;
        }
        if(right < heapSize && a[right] > a[parent])  
        {
            parent = right;
        }
        //将三者最大值跟父节点调换，但是不考虑左右子结点谁大谁小
        if(parent != i) {      
            int temp = a[parent];
            a[parent]=a[i];
            a[i]=temp;           
            //当换了爸爸以后，看被换掉的儿子的儿子是不是也要换
            maxHeapfy(a,parent,heapSize);    
        }
    }
    static void buildMaxHeap(int []a,int heapSize) {
        for(int i = (heapSize-2)/2;i >= 0;i--) {
            maxHeapfy(a,i,heapSize);
        }
    }
    static void heapSort(int []a) {
    	 int len = a.length-1;
    	 //初始化堆
         buildMaxHeap(a,len);
         
         for(int i =len;i>0;i--) {
        	 //对调最大的和最后一个结点
        	 int temp =a[0];
             a[0]=a[len];
             a[len]=temp;  
             len--;
             //最大值已确定，总长度减1迭代
             maxHeapfy(a,0,len);
         }
      
    }
    
	 public static void main(String args[]) {
		 int []a = {18,11,9,7,3,4,2,2,3,9};
	        heapSort(a);
	        System.out.println(Arrays.toString(a));
	    }
	 
	 
}
//结果：[2, 2, 3, 3, 4, 7, 9, 9, 11, 18]