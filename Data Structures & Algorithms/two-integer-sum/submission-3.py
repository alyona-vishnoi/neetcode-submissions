class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}

        for i, n in enumerate(nums):
            # i is index
            # n is value
            diff = target - n
            
            if diff in hash1:
                return [hash1[diff],i]

            # store index of value, 
            # if value is not unique, store most recent index
            hash1[n] = i
            

        