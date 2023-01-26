class Solution(object):
    def moveZeroes(self, nums):
        length = len(nums)
        
        left = 0
        
        for _ in range(length):
            if nums[left] == 0:
                del nums[left]
                nums.append(0)
                continue
            
            left += 1
            

''' 투 포인터 솔루션
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1   
'''