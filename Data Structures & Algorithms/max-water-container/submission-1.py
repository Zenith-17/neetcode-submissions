class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        ans = 0

        while p1 < p2:
            ans = max(
                ans,
                min(heights[p1], heights[p2]) * (p2 - p1)
            )

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1

        return ans