class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # hashmap, count each char
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) # O(n)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
               return "" 
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        
        return res

        # cnt = Counter(s)                                  # e.g. {'a':2,'b':1}
        # n = len(s)

        # # If any char appears more than ceil(n/2), impossible
        # if max(cnt.values()) > (n + 1) // 2:              # pigeonhole check
        #     return ""

        # # Build array of size n, fill even indices first, then odd
        # res = [''] * n                                    # placeholder array
        # # Sort chars by frequency descending
        # items = sorted(cnt.items(), key=lambda x: -x[1])  # [('a',2),('b',1)]
        # i = 0                                             # write pointer

        # for ch, k in items:                               # place all copies of each char
        #     while k > 0:
        #         if i >= n:                                # when even slots done, move to odd
        #             i = 1
        #         res[i] = ch                               # put char at position i
        #         i += 2                                    # skip one to avoid adjacency
        #         k -= 1

        # return "".join(res) 