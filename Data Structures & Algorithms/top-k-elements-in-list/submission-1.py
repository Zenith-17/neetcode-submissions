from collections import Counter

class Solution:
    def topKFrequent(self,nums, k):
        count = Counter(nums)
        
        # bucket[i] = list of elements with frequency i
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # right to left
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result