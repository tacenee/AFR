/**
 * 
 * @author Tacenee
 *
 */
public class GuiBingTest {	
	public static void main(String[] args) {
		int[] a= {2,4,9,6,1,3,5,8,7};
		GuiBing(a);
		System.out.println(Arrays.toString(a));
	}
	
	private static void GuiBing(int[] a) {		
		GB(a,0,a.length-1);
	}
	/**
	 * 
	 * @param a 需排序的数组
	 * @param start 排序起始位置
	 * @param end 排序结束位置
	 */
	private static void GB(int[] a,int start,int end) {
		// TODO Auto-generated method stub
		int middle=(start+end)/2;
		if(start<end) {
			GB(a,start,middle);
			GB(a,middle+1,end);
			GuiBingDG(a,start,end);
		}
	}
	
	private static void GuiBingDG(int[] a,int L,int R) {
		// TODO Auto-generated method stub
		int[] temp =new int[a.length];
		int k =L;
		int mid = (L+R)/2;
		int p1=L;
		int p2=mid+1;
		while(p1<=mid&&p2<=R) {
			if(a[p1]<=a[p2]) {
				temp[k++]=a[p1++];
			}else {
				temp[k++]=a[p2++];
			}
		}
		
		while(p1<=mid) {temp[k++]=a[p1++];}
		while(p2<=R) {temp[k++]=a[p2++];}
		
		for(int i=L;i<=R;i++) {
			a[i]=temp[i];
		}
	}
}