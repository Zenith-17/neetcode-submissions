class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pp=[1]*n
        sp=[1]*n

        pp[0],sp[n-1]=nums[0],nums[n-1]

        for i in range(1,n):
            pp[i]=pp[i-1]*nums[i]
        
        for i in range(n-2,-1,-1):
            sp[i]=sp[i+1]*nums[i]

        ans=[]

        for i in range(0,n):
            p1=pp[i-1] if i >0 else 1
            p2=sp[i+1] if i<n-1 else 1

            ans.append(p1*p2)

        return ans
        
        