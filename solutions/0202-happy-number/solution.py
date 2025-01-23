class Solution:
    def isHappy(self, n: int) -> bool:
        def loop(n):
            k = 0
            while n > 0:
                rem = n % 10
                k = k + rem**2
                n = n//10
            return k
        
        seen = set()
        while n!=1:
            n = loop(n)
            if n in seen:
                return False
            seen.add(n)
        return True
