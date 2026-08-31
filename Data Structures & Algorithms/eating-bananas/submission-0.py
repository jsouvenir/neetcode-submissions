class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        
        fastest = r

        while l<=r:
            k = (r+l) // 2
            sum = 0

            for i in range(len(piles)):
                sum += math.ceil(piles[i]/k)

            if sum <= h:
                    fastest = min(fastest,k)
                    r = k-1
                    
            else:
                    l = k+1
        return fastest
