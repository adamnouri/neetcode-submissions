class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set s = new HashSet<>();
        for(int i = 0; i<nums.length; i++){
            s.add(nums[i]);
        }
        return !(s.size() == nums.length);
    }
}