class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
          result = ''
          while columnNumber > 0:
            columnNumber -= 1
            reman = columnNumber % 26
            result = chr(65 + reman) + result 
            columnNumber = columnNumber // 26
          return result  
