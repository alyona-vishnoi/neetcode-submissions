class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get non duplicates
        # sort
        # somehow track the longest consequtive sequence

        if not nums:
            return 0

        if len(nums) == 1:
            return 1
        nondupes = set(nums)
        sortnums = list(sorted(nondupes))

        tracker = [1]

        count = 1

        for i in range(len(sortnums) - 1):
            if sortnums[i] + 1 == sortnums[i+1]:
                count += 1
            else:
                count = 1
            tracker.append(count)

        return max(tracker)




