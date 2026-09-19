class Solution:
    def binarySearch(self, left, right, nums, target):
        l, r = left, right

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1 
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums) 
        l, r = 0, length - 1
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l += 1
        if nums[-1] < target:
            return self.binarySearch(0, l, nums, target)
        return self.binarySearch(l, (length - 1), nums, target)
    

