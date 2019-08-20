import java.util.ArrayList;
import java.util.Arrays;

public class offer40_只出现1次的两个数 {
    ArrayList<Integer> list = new ArrayList<Integer>();
    public void FindNumsAppearOnce(int [] array,int num1[] , int num2[]) {
        Arrays.sort(array);
        for(int i=0;i<array.length;i++){
            if((i+1)<array.length && array[i]==array[i+1]){
                i++;
            }else{
                list.add(array[i]);
            }
        }
        num1[0]=list.get(0);
        num2[0]=list.get(1);
    }
}
