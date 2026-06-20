class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = "ababd" l = 0, r = 0 res = ""
        # a res = "a" r+1
        # ab res = "a" r+1
        # aba res = "aba" r+1
        # abab res = "aba" r+1
        # ababd res = "ababd" r+1
        # s = "abbc" l = 0, r = 0 res = ""
        # a res = "a" r+1
        # 1. ab res = "a" r+1
        # abb res = "a" r+1
        # abbc res = "a" r+1
        # 2. ab res = "a" l+1 r+1
        # bb res = "bb" r+1 or l+1 r+1
        # algorithm
        # base case 1: l == n ret 0
        # base case 2: r == n ret dfs(l+1, r)
        # base case 3: s[l] == s[r] and isPalindromic(s[l:r+1]) update longest string max(len(longest), s[l:r+1])

        longest = ""
        def isPalindromic(s2):
            l, r = 0, len(s2)-1
            while l < r:
                if s2[l] != s2[r]:
                    return False
                l += 1
                r -= 1
            return True
        cache = {}
        def dfs(l, r):
            nonlocal longest
            if l == len(s):
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            if r == len(s):
                return dfs(l+1, r)
            if s[l] == s[r]:
                substring = s[l:r+1]
                if len(substring) >= len(longest) and isPalindromic(substring):
                    longest = substring[:]
            cache[(l, r)] = max(dfs(l, r+1), dfs(l+1, r+1))
            return cache[(l, r)]
        dfs(0, 0)
        return longest
                

        