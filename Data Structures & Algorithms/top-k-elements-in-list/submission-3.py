class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i,0)

        # index is count, value is input
        bucket = []
        # init
        for i in range(len(nums)+1):
            bucket.append([])
            # we do an empty list, bc multiple/none items can have that frequency
        
        for val in hashMap:
            bucket[hashMap[val]].append(val)

        sol = []
        for i in bucket[::-1]:
            for j in i:
                sol.append(j)
                if len(sol) == k:
                    return sol

        