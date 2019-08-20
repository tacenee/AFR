public class offer01_二维数组中查找 {
    public boolean Find(int target, int [][] array) {
        int i = array.length - 1;
        int j = 0;
        while(i >= 0 && j < array[0].length){
            if(array[i][j] == target){
                return true;
            }else if(array[i][j] > target){
                i--;
            }else{
                j++;
            }
        }
        return false;
    }
}
