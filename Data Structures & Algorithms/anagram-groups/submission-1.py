class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # set(act) -> act, cat
        groups = defaultdict(list)
        for s in strs:
            # strs = ["act","pots","tops","cat","stop","hat"]
            # groups["act"] = [act, ]
            # "a : 1, b : 0, c: 1 ... t : 1" each counter size  26
            anagram = [0] * 26
            for c in s:
                anagram[ord(c)-ord('a')] += 1
            groups[tuple(anagram)].append(s)
        res = []
        for group in groups.keys():
            res.append(groups[group])

        return res
        