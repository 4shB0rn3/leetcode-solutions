class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # jakc = int(''.join(map(str, digits))) + 1
        return list(map(int, str((int(''.join(map(str, digits))) + 1))))

