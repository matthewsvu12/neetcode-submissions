class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryN = bin(n)[2:]
        count = 0
        for i in range(len(binaryN)):
            if binaryN[i] == '1':
                count += 1
            
        return count
        