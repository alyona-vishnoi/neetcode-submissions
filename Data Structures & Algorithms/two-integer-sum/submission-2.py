class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}

        for i, n in enumerate(nums):
            # i is index
            # n is value
            diff = target - n
            
            if diff in hash1:
                return [hash1[diff],i]
            hash1[n] = i
            

        