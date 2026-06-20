class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        c1 = Counter(s1)
   
        for i in range(len(s2)-len(s1)+1):
            if s2[i] in c1 and Counter(s2[i:i+len(s1)]) == c1:
                return True
  
        return False
        