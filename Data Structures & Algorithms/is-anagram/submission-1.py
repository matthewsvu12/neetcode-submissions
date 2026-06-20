class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        for c in s:
            count1[ord(c) - ord('a')] += 1
        for c in t:
            count2[ord(c) - ord('a')] += 1

        return count1 == count2
        