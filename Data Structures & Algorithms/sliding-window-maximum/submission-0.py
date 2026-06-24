from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        ans = []

        for i in range(len(nums)):
            # Remove indices outside window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Maintain decreasing deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Front contains max of current window
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans