class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Input: s = "XYYX", k = 2, Output: 4
        # s = "XYYX ZZZZK"
        # XYYX l = 0, r = 3
        # YYX  l = 1, r = 3 map['Y'] -= 1, k++
        # YX   l = 2, r = 3 map['Y'] -= 1, k++
        # X   l = 3, r = 3
        # XZ  l = 3, r = 4. map['Z'] += 1 k--
        # XZZ l = 3, r = 5. map['Z'] += 1 k--
        # XZZZ -> ZZZ l = 3, r = 6 slide while s[l] != s[r]: map['X'] -= 1, k++, l += 1
        # ZZZZ l = 4, r = 7
        # ZZZZK l = 4, r = 8

        # sliding window
        # left and right pointer
        l = 0
        longest = 0
        charCnt = Counter()
        originalK = k
        maxf = 0
        for r in range(len(s)):
            charCnt[s[r]] += 1
            maxf = max(maxf, charCnt[s[r]])

            # shrink window
            while (r - l + 1 - maxf) > k:
                charCnt[s[l]] -= 1
                l += 1
        
            print(s[l:r+1])
            longest = max(longest, r - l + 1)
            print(longest, k)


        
        return longest
        