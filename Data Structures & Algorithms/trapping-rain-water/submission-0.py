class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        pge = [0]
        nge = [0] * n
        nge[n - 1] = n - 1

        for i in range(1, n):
            if height[pge[i - 1]] >= height[i]:
                pge.append(pge[i - 1])
            else:
                pge.append(i)

        for i in range(n - 2, -1, -1):
            if height[nge[i + 1]] >= height[i]:
                nge[i] = nge[i + 1]
            else:
                nge[i] = i

        ans = 0

        for i in range(n):
            leftMax = height[pge[i]]
            rightMax = height[nge[i]]
            ans += min(leftMax, rightMax) - height[i]

        return ans