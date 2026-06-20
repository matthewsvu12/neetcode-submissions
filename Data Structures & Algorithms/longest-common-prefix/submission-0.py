class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        idx = 0

        for i in range(1, len(strs)):
            print(strs[i])
            j = 0
            while j < min(len(strs[i]), len(lcp)) and strs[i][j] == lcp[j]:
                j += 1
            lcp = lcp[:j]

            # for j in range(min(len(strs[i]), len(lcp))):
            #     if strs[i][j] != lcp[j]:
            #         lcp = lcp[:j]
            #         print(lcp)
            # iterate through strs
            # compare if lcp is the same as current string index, if they are update LCP
            # break once they aren't equal
          
        return lcp