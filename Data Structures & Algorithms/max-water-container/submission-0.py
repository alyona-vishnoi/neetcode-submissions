class Solution:
    def maxArea(self, heights: List[int]) -> int:
        prev = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            curr = min(heights[left], heights[right]) * (right - left)

            if curr > prev:
                prev = curr

            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1

        return prev
        