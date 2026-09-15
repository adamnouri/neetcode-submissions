class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> s = new HashMap<>();
        for(int i = 0; i<nums.length;i++){
            s.put(target-nums[i], i);
        }
        for(int i = 0; i<nums.length;i++){
           if(s.get(nums[i]) != null && !s.get(nums[i]).equals(i)){
            return new int[]{i, s.get(nums[i])};
           }
        }
        return null;
    }
}
/*
I want to get enter the value I need and return the index
*/