class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        
        res = []
        for i in range(k):
            m = float("-inf") # max frequency
            v = 0 #most frequent number
            for key in frequency:
                if frequency[key] > m:
                    m = frequency[key]
                    v = key
            res.append(v)
            frequency.pop(v)
        
        return res
