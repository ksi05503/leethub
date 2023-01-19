class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        copy = list(nums)
        length = len(nums)
        
        for i in range(length):
            targetIndex = (length-k+i) % (length)
            nums[i] = copy[targetIndex]
        
        
        # 0,1,2,3,4,5,6