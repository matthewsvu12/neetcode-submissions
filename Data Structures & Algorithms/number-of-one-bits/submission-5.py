class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryN = bin(n)
        count = 0
        for i in range(2, len(binaryN)):
            if binaryN[i] == '1':
                count += 1
        return count
        # for i in range(32):
        #     if (n & (1 << i)):
        #         count += 1
            
        # return count
        