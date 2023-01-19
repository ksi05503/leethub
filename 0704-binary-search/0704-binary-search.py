class Solution(object):
    def search(self, nums, target):
        length = len(nums)

        left = 0
        right = length-1

        
        while right >= left:
            mid = int(( right + left ) / 2)

            if nums[mid] > target:
                right = mid - 1
                continue

            elif nums[mid] < target:
                left = mid + 1
                continue
            
            else:
                return mid

        return -1

            
            
            
            