class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = defaultdict(int) 
        longest = 0

        for r,c in enumerate(s):
            if c in seen:
                l = max(seen[c] + 1, l) 
                
            longest = max(longest, r-l + 1) 
            seen[c] = r 
    
        return longest

            