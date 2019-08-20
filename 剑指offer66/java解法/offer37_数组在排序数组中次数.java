public class offer37_数组在排序数组中次数 {
    public int GetNumberOfK(int [] array , int k) {
        int len = array.length;
        int count = 0;
        for(int i = 0; i < len; i++){
            if(array[i] == k) count++;
            if(array[i] > k) break;
        }
        return count;
    }
}
