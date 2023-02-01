class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s= list(s)
        if len(s) ==1:
            return 1
        
        seen = {} 
        
        result = 0
        current = 0
        
        i=0
        while i <= len(s)-1:
            if s[i] in seen:
                i = seen[s[i]] + 1
                seen = {}
                
                result = max(current, result)
                current = 0
                continue            
            
            current += 1
            seen[s[i]] = i
            i += 1
            
        return max(current, result)
            
            
            