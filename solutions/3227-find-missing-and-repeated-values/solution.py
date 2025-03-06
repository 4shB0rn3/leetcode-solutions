class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        flattened = sum(grid,[])
        count = [0]*(len(flattened)+1)

        for num in flattened:
            count[num] += 1
        
        omitted = count[1:]

        for i in range(len(count[1:])):
           if omitted[i] == 2:
               a = i + 1
           if omitted[i] == 0:
               b = i + 1
        
        return [a,b]
