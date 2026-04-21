class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i,0)

        sol = []
        while k != 0:
            max_f = (0,0)
            for key in hashMap:
                if hashMap[key] >= max_f[0]:
                    max_f = (hashMap[key],key)
            sol.append(max_f[-1])
            del hashMap[max_f[-1]]
            k -=1
        return sol
        