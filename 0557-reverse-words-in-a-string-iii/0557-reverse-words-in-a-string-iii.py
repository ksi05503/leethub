class Solution(object):
    def reverseWords(self, s):
        sList = list(s)
        
        # reverse chars first
        left, right = 0, len(s)-1
        
        while right > left:
            sList[left], sList[right] = sList[right], sList[left]
            left += 1
            right -= 1
        
        s = ''.join(sList)
        
        words = s.split(' ')
        
        left2, right2 = 0, len(words) - 1
        
        while right2 > left2:
            words[left2], words[right2] = words[right2], words[left2]
            left2 += 1
            right2 -= 1
            
        return ' '.join(words)

            
            
            