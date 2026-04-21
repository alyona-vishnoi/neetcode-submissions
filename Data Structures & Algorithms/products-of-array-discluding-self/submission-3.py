class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1]
        postfix = [1]

        reversednums = list(reversed(nums))

        for i in range(1,n):
            prefix.append(prefix[i-1] * nums[i - 1])

        for i in range(1,n):
            postfix.append(postfix[i-1] * reversednums[i - 1])

        postfix = list(reversed(postfix))

        result = []
        for i in range(n):
            result.append(prefix[i] * postfix[i])

        return result
