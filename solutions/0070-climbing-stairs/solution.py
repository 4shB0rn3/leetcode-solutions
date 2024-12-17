class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return n 
        val = {1: 1,
          2: 2,
          }
        count = 3 
        a, b = 1, 2
        while(count<=n):
            sum = a + b
            val[count] = sum
            a, b = b, sum
            count += 1
        return val[n]
