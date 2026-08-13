class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cur = set()
        for i in nums:
            cur.add(i)

        if len(cur) == len(nums):
            return False
        else:
            return True


