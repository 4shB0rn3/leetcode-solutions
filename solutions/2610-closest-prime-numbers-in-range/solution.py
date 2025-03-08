class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False 

        p = 2
        while p * p <= right:
            if is_prime[p]:
                for i in range(p * p, right + 1, p):
                    is_prime[i] = False
            p += 1
        
        primes_list = []
        for p in range(max(2, left), right + 1):
            if is_prime[p]:
                primes_list.append(p)
        
        if len(primes_list) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        result = [-1, -1]

        for i in range(len(primes_list) - 1):
            gap = primes_list[i + 1] - primes_list[i]
            if gap < min_gap:
                min_gap = gap
                result = [primes_list[i], primes_list[i + 1]]

        return result
