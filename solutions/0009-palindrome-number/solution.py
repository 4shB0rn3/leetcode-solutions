class Solution:
    def isPalindrome(self, x: int) -> bool:
      if x < 0:
          return False

      num = x
      k = 0
      while(x): 
          k = k * 10 + x % 10
          x = x//10
        
      if num == k :
          return True
      return False

