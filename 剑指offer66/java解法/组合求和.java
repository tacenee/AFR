class Solution {
public List<List<Integer>> combinationSum(int[] candidates, int target) {
	List<List<Integer>> result = new ArrayList<>();
	List<Integer> list = new ArrayList<>();
	
	Arrays.sort(candidates);
	combinationSumHelp(candidates,result,list,target,0);
	return result;
}
 
public boolean combinationSumHelp(int[] candidates,List<List<Integer>> result,List<Integer> list,int target,int start){
	if(target<0){
		return false;
	}else if(target==0){
		List<Integer> temp = new ArrayList<Integer>(list);
		result.add(temp);
		return false;
	}else{
		for(int i = start; i < candidates.length ; i++){
			list.add(candidates[i]);
			boolean flag = combinationSumHelp(candidates,result,list,target-candidates[i],i);
			list.remove(list.size()-1);
			if(!flag){
				break;
			}
		}
}
	return true;
}
}
