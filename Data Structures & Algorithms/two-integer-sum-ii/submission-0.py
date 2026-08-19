class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers if left pointer is less than target then increment
        #else increment right pointer
        p1 = 0
        p2 = len(numbers) - 1
        sum = 0
        
        while p1 <= p2:
            sum = numbers[p1] + numbers[p2]
            if sum > target:
                p2 -= 1
                
            elif sum < target:
                p1 += 1
                
            else:
                return [p1 + 1, p2 + 1]