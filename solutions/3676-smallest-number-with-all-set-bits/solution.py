class Solution:
    def smallestNumber(self, n: int) -> int:
           bry = bin(n)[2:]
           cc = ['1' if x == '0' else x for x in list(str(bry))]
           return int((''.join(cc)),2)
           
