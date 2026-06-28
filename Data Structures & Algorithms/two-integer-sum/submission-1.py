class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashnums = {}
        for i in range(len(nums)):
            if target - nums[i] in hashnums:
                return [hashnums[target - nums[i]], i]
            hashnums[nums[i]] = i