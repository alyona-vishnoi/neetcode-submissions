class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]: 
                # in sorted so we check whether to search left or right
                if target > nums[mid] or target < nums[l]:
                    # bc rotated we have two conditionals
                    # we want to search the right half
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # so nums[l] > nums[mid] and so mid onwards sorted
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 # want to search left
                else:
                    l = mid + 1
        return -1




        