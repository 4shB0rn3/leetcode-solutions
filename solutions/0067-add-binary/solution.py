class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        x = a.zfill(max(len(a), len(b)))
        y = b.zfill(max(len(a), len(b)))
        m = int(x,2)
        n = int(y,2)
        sum = m + n
        z = []
        while(sum):
            k = sum % 2
            z.append(k) 
            sum = sum // 2
  
        dd = z[::-1]
        # print(dd)
        sh = ''.join(map(str,dd))
        return sh
