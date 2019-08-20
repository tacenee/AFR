/**
*冒泡排序
*它重复地走访过要排序的数列，一次比较两个元素，
*如果它们的顺序错误就把它们交换过来。
*走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成
*/
public arr bubble(int[] arr){
	int temp;
	int size=arr.length;
	//i考虑的是一共有多少个位置
	for(int i =0;i<size-1;i++){
		//j考虑的是每个位置开始剩下要对比的次数
		for(int j=0;j<size-1-i;j++){
			if(arr[j+1]<arr[j]){
				temp=arr[j+1];
				arr[j+1]=arr[j];
				arr[j]=temp;
			}
		}
	}
}