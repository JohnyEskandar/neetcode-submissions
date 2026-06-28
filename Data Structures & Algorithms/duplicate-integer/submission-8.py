class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set with nums seen
        # if see number again return true else false   
        return len(set(nums)) < len(nums)