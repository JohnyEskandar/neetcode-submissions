class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set()
        for i in nums:
            setlen = len(sett)
            sett.add(i)
            if setlen + 1 != len(sett):
                return True
        
        return False
