class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.capacity = len(nums)
        self.capacity = 2*self.capacity
        ans = [0]*self.capacity
        j = 0
        for i in range(len(ans)):
            ans[i] = nums[i % len(nums)]  
        return ans

