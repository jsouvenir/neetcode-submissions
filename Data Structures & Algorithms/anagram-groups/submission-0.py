class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert words into freq counters of letters
        # store counters as keys
        # convert count into a tuple so it can be used as a key
        # append words to values 
        # convert view object into list 

        result = defaultdict(list)  
        for s in strs: # O(m)
            count = [0] * 26 # O(26) constant time

            for c in s: # O(n)
                count[ord(c)- ord("a")] +=1

            result[tuple(count)].append(s)

        return list(result.values())




                
                


            

        