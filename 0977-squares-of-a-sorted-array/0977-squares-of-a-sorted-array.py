class Solution(object):
    def sortedSquares(self, nums):
        length = len(nums)
        result = []

        while length > 0:
            left = pow(nums[0],2)
            right = pow(nums[length-1],2)

            if left >= right:
                result.insert(0,left)
                nums.pop(0)
            else:
                result.insert(0,right)
                nums.pop()
            length -= 1

        return result

        # sorted_list = [0] * length 로 먼저 메모리를 할당해뒀다면 insert 비용을 줄일 수 있었다.
        