class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # pos = neg = 0
        # for num in nums:
        #     if num > 0:
        #         pos += 1
        #     elif num < 0:
        #         neg += 1
        neg = sum(1 for x in nums if x < 0)
        pos = sum(1 for x in nums if x > 0)
        return max(pos,neg)
        
