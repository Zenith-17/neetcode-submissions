from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        d2=dict(d)
        d3=sorted(d2.items(),key= lambda x:-x[1])
        print(d3)
        ans=[]
        for x in d3[:k]:
            ans.append(x[0])
        return ans   