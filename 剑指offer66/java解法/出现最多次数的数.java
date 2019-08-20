public class FindMastNum{
	public static int findMastNum(int[] a){
		Arrays.sort(a);
		int len = a.length;
		int midNum = a[len/2];
		int count = 0;
		for(int i=0;i<len;i++){
			if(a[i]==midNum){
				count++;
			}
		}
		return count!=0?midNum:0;
	}
	
	public static main(String[] args){
		int[] a = {1,2,3,2,2,2,4,3};
		System.out.println(findMastNum(a));
	}
}