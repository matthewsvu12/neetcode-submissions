class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryN = bin(n)[2:]
        return bin(n).count('1')
        count = 0
        for i in range(32):
            if (n & (1 << i)):
                count += 1
            
        return count
        