class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(speed):
            s=0
            for pile in piles:
                s+=int(math.ceil(pile/speed))
            return s<=h

        #binary search answer possible format 
        l,r=1,max(piles)
        ans=-1

        while l<=r:
            m=(l+r)//2

            if valid(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans

        