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



''' 일부러 직접 구현했는데, 파이썬스럽게 요약하면 아래와 같다.
        words = s[::-1].split()
        return " ".join(list(reversed(words)))

    다른 답변들과 달리 먼저 전체 s 를 통째로 reverse 시키면 시간복잡도를 O(n) 으로 줄일 수 있다.
'''

            
            
            