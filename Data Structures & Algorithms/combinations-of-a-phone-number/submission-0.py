class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 1. make dict {2 : "abc", 3: "def", 4: "ghi", 5: "jkl" , 6: "mno" , 7: "pqrs" , 8: "tuv" , 9: "wxyz"}
        # 2. do a dfs where we initially have a string a param. This will be added to as we recurse through the decision tree.
        # 3. our base case is when the len(digits) == len(combo)
        # 4.  
        if len(digits) == 0:
            return []
        letters = {2 : "abc", 3: "def", 4: "ghi", 5: "jkl" , 6: "mno" , 7: "pqrs" , 8: "tuv" , 9: "wxyz"}
        res = []
        def dfs(combo: str):
            if len(combo) == len(digits):
                res.append(combo)
                return
            # digits = "34"
            # combo = "" len == 0
            # combo = "d" len == 1
            # combo = "dg" len == 2 append to res
            # combo = "d" len == 1
            # combo = "dh" len == 2 append to res
            curr_digit = digits[len(combo)]
            print(curr_digit)

            for c in letters[int(curr_digit)]:
                dfs(combo + c)
        dfs("")
        return res
        
        