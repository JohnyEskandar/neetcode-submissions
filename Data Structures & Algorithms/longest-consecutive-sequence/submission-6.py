class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # can use a hashmap where the val is an indicator 
        # 0 1 2 3 4 
        if len(nums) == 0:
            return 0
        snums = sorted(set(nums))
        consec = [0] * len(snums)
        consec[0] = 1
        for i in range(1, len(snums)):
            if (snums[i] == snums[i-1]+1):
                consec[i] = consec[i-1] + 1
            else:
                consec[i] = 1
        
        sconsec = sorted(consec)
        res = sconsec[-1]
        return res