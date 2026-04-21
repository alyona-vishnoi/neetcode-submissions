class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                prod *= i
            if i == 0:
                zero_count += 1

        output = [ prod for i in range(len(nums)) ]

        zero_flag = 1

        if zero_count >= 1:
            zero_flag = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                output[i] = (output[i] * zero_flag) // nums[i]
            else:
                if zero_count > 1:
                    output[i] = 0

        return output
        




        