class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        n = bin(n)[2:]
        print(n)
        count = 0
        for i in range(len(n)):
            if n[i] == '1':
                count += 1
            
        return count
        