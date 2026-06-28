class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        for i, n in enumerate(nums):
            if target - n in indicies:
                return [indicies[target - n], i]
            indicies[n] = i
        

        # make hashmap to store num -> index
        # as going thorugh and populating the hashmap
            # check if target - current n is in the hashmap
            # return the index of target - n, index of current
        