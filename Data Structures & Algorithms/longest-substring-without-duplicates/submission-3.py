class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Input: s = "zxyzxyz"
        set? can't do it because we don't know the position
        hashmap of indices of each character
        ex 'z' : [0, 3]
        find longest distance between two points without duplicate characters
        zxxyz
        z: [0, 4]
        x: [1, 2]
        y: [3]
        (2, 4)
        output should be 3 since len('xyz') = 3

        s = 'z' = 1
        s = 'zx' = 2
        s = 'zxy' = 3
        s = 'zxyy' = 3 check hashmap: found dup, remove all elements in the set up UNTIL the duplicate 
        map(z:0 x:1 y:2)  -> map(y:3)

        1. when do we update our map: ans: when we find duplicate in our map
        2. when do we update longest distance w/o dup characters so far?
        """
        longestYn = 0
        l = 0
        yn = defaultdict(list)
        # s = "zxyzxyz"
        """
            yn = {z: [0, 3], x: [1], y : [2]}
            zxyzxyz
             l
               r
            zxyzxyz
        """
        for r, c in enumerate(s):
            if c in yn:
                prev = yn[c][-1]
                if prev >= l:
                    l = prev+1
            
            longestYn = max(longestYn, r-l+1)
            yn[c].append(r)
        
        return longestYn
           



        