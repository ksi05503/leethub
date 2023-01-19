class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums)
        
        left = 0
        right = length -1
        mid = 0

        while right >= left :
            mid = int((right + left) / 2)

            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid 

        if nums[mid] < target:
            return mid +1
        else:
            return mid

        