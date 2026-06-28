class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            correct = nums[i] - 1

            if nums[i] == i + 1:
                i += 1
            elif nums[correct] == nums[i]:
                return nums[i]
            else:
                nums[i], nums[correct] = nums[correct], nums[i]

        return -1