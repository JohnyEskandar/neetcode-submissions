class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # so array of tasks from A-Z
        # n cycles between same tasks
        # one thing is use a hashmap to track frequencies
        # ex: n = 1, A, A, A, B, B, C, C
        # A - B - C - A - B - C - A ---> if n < count of dif task: then ans = len of tasks
        # if n = count of dif tasks: then ans = (highest freq)*n + count of other freq = to highest freq
        # if n > count of dif tasks: then 
        # A, A, A, n = 2 
        # A - idle - idle - A - i - i - A = 7 
        # A i i A i i A i i A = 10
        count = Counter(tasks)

        if n+1 < len(count):
            ans = len(tasks)
        elif n+1 == len(count):
            hFreq = max(count.values())
            hFreqC = 0
            for key, value in count.items():
                if value == hFreq:
                    hFreqC += 1
            ans = (hFreq - 1)*(n+1) + hFreqC

            # keymax, hfreq = max(count.items())
            # count.pop(count[keymax])
            # ans = hfreq*n
            # secHfreq = max(count.values())
            # if secHfreq == 
        else:
            hFreq = max(count.values())
            hFreqC = 0
            for key, value in count.items():
                if value == hFreq:
                    hFreqC += 1
            ans = (hFreq - 1)*(n+1) + hFreqC

        return ans