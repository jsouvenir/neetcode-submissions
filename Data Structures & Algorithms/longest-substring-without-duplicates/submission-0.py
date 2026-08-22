class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = set()

        for index,char in enumerate(s):
            #check for duplicates
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            longest = max(longest, index-l+1)
        return longest
            



