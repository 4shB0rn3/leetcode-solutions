class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = sorted(nums)
        for i in range(len(num)):
            if i != num[i]:
                return i
        if len(num) not in num:
            return len(num)
