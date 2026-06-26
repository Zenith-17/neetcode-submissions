class Solution:
    def findMin(self, nums: List[int]) -> int:
        # question to ask is nums[mid]>nums[n-1]
        n=len(nums)
        s,e=0,n-1
        while s<e:
            m=(s+e)//2
            if nums[m]<=nums[n-1]:
                e=m
            else:
                s=m+1
        return nums[e]
        