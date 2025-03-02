class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 :
            return 0
        
        left, right = 1, x

        while left <= right:
            mid = left + (right - left)//2
            mid_sqrd = mid * mid

            if mid_sqrd == x:
                return mid
            elif mid_sqrd > x:
                right = mid - 1 
            else:
                left = mid + 1
            
        return right
