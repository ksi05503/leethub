class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {} 
        
        result = 0
        current = 0
        
        i=0
        while i <= len(s)-1:
            if s[i] not in seen:                
                current += 1
                seen[s[i]] = i
                i += 1
            else:    
                i = seen[s[i]] + 1
                seen = {}
                result = max(current, result)
                current = 0
            
        return max(current, result)
            
            
            