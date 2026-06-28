class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set with nums seen
        # if see number again return true else false   
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False