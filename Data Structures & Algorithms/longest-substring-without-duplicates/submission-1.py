class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        # zxx
        #  l
        #   r
        # two pointer, left and right @ index 0
        # keep track of current longest with a set that will be removed and added to.
        # right pointer will increment at end of loop
        # if s[r] in seen: l += 1, seen.remove(s[l])
        # return max(longest, r - l + 1)

        l, r, = 0, 0
        # zxyzxyz
        # seen = {z, x, y}
        # longest = 3
        while r < len(s):
            # s[r] is in the non-duplicate char window, so we remove it from the seen set
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            longest = max(longest, r - l + 1)
            seen.add(s[r])
            r += 1
    
        return longest

        