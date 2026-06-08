class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest= 1
        current = 1
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                current +=1
            else:
                longest = max(current, longest)
                current = 1
        longest = max(current, longest)
        return longest