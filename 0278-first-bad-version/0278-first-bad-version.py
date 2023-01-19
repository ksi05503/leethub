# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        
        left = 1
        right = n
        mid = int((right+left)/2)

        while right > left:            
            if isBadVersion(mid):
                right = mid 
            else:
                left = mid + 1

            mid = int((right+left)/2)



        return mid