class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) #key is number value is frequency
        #creates buckets
        buckets = [[] for i in range(len(nums) + 1)]
        #freq counter
        for num in nums:
            count[num] += 1
        #maps freq to bucket indicies and appends num
        for n, c in count.items():
            buckets[c].append(n)

        result = []
        #starts from the back of buckets decrementing and storing 
        #bucket into result list stopping at the k most frequent
        for i in range(len(buckets)-1, 0, -1):

            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result

            

        



