class Solution(object):
    def twoSum(self, numbers, target):
        # 정렬된 two sum -> 양끝부터 좁히면 모든 경우를 O(n) 으로 묶을 수 있음
        length = len(numbers)

        left, right = 0, length - 1
        sum = numbers[left] + numbers[right]

        while sum != target:
            if sum < target:
                left += 1
            else:
                right -= 1
            sum = numbers[left] + numbers[right]

        return [left + 1, right + 1]


''' 출제의도는 아닌것같지만 해시맵을 이용한 재밌는 풀이. 
    (현재 값을 뺀 녀석과 인덱스를 저장해두고, 나머지가 발견되면 return)
    
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = dict()
        for i in range(len(numbers)):
            
            remaining = target - numbers[i]
            #if remaining == numbers[i]:
            #    continue
            if remaining in hashmap:
                return [(hashmap[remaining]+1), (i+1)]
            hashmap[numbers[i]] = i
'''
        
        
        
        
        