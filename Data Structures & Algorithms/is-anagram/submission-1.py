class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_1 = defaultdict(int)
        map_2 = defaultdict(int)

        for c in s:
            map_1[c] += 1
        for c in t:
            map_2[c] += 1

        if map_1 == map_2:
            return True
        else:
            return False

