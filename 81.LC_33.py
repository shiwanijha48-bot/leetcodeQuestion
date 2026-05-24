class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0   # starting index
        high = len(nums) - 1     # ending index
        while low <= high:       # binary search loop
            mid = (low + high) // 2   # middle index
            if nums[mid] == target:   # target found
                return mid
            if nums[mid] <= nums[high]:  # check if right half is sorted
                if nums[mid] <= target <= nums[high]:  # target lies in right sorted half
                    low = mid + 1
                else:   # target lies in left half
                    high = mid - 1
            else:   # otherwise left half is sorted
                if nums[low] <= target <= nums[mid]:    # target lies in left sorted half
                    high = mid - 1
                else:     # target lies in right half
                    low = mid + 1
        return -1         # target not found
