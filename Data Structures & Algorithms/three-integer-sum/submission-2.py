class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i,n in enumerate(nums):
            l = i+1
            r = len(nums) -1
            while r > l:
                add = n + nums[r] + nums[l]
                
                if add == 0 and [n, nums[r], nums[l]] not in ans:
                    ans.append([n, nums[r], nums[l]])
                if add > 0:
                    r = r - 1
                else:
                    l = l + 1
        
        return ans
