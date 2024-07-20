class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        elif nums[-1] < target:
            return len(nums) - 1
        else:
            for idx, i in enumerate(nums):
                if i > target:
                    return idx


obj = Solution()
print(obj.searchInsert([10, 20, 30, 40, 50], 55))
