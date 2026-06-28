class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li = 0
        ri = len(numbers) - 1
        r = numbers[ri]
        l = numbers[li]
        # while r >= target:
        #     ri -= 1
        #     r = numbers[ri]
        while l + r != target:
            if l + r < target:
                li += 1
                l = numbers[li]
            if l + r > target:
                ri -= 1
                r = numbers[ri]
        
        return [li + 1, ri + 1]

            