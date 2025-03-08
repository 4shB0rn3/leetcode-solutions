class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
            n = len(blocks)
            minVal = n
            p = 0
            while((p+k)<= n):
                count = 0
                for i in range(p,k+p):
                    if blocks[i] == 'W':
                        count += 1

                if count < minVal :
                    minVal = count

                p += 1

            return minVal
