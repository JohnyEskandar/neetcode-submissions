class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ans = -1000
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r+l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]