class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        left = 0
        right = left + 1
        n = len(prices)
        while right < n:
            if prices[left] < prices[right]:
                # if price we buy < price we sell we might be able to make a profit
                currDiff = prices[right] - prices[left]
                maxDiff = max(currDiff, maxDiff)
            else:
                # buy > sell, move pointer to sell
                left = right
            right +=1

        return maxDiff
