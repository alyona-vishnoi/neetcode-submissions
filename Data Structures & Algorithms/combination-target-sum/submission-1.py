class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []
        path = []
        n = len(nums)

        def backtrack(i, remaining):
            if remaining == 0:
                current = path.copy()
                answer.append(current)
                return

            for j in range(i, n):
                value = nums[j]
                if value > remaining:
                    break # will go to next
                path.append(value)
                # since we can try as many
                backtrack(j, remaining - value)
                path.pop()

        backtrack(0, target)
        return answer


        