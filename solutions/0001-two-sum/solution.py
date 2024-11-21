class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i in range(len(nums)):
           compare = target - nums[i]

           if compare in seen:
              return [seen[compare],i]

           seen[nums[i]] = i
