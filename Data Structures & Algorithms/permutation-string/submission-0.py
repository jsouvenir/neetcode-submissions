class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = len(s1)
        s1_count = [0] * 26
        s2_count = [0] * 26

        #increment count array for letters in window
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        matches = 0 

        #find matches
        for i in range(26):
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        l = 0
        #start r pointer at end of window
        for r in range(len(s1), len(s2)):
            #check for matches
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            l += 1

        return matches == 26
                


