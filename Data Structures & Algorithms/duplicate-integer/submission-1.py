class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for i in nums:
            if i not in x:
                x[i] = True
            else:
                return True
        return False