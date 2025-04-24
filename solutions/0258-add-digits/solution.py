class Solution:
    def addDigits(self, num: int) -> int:
        count = 0
        if num < 10:
            return num
        else:
        #    res = sum(list(map(int,str(num))))
           res = sum(int(digit) for digit in str(num))
           return self.addDigits(res)
