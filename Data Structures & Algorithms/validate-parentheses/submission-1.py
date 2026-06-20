class Solution:
    def isValid(self, s: str) -> bool:
        """
        "([{}])"

        stk = [')', ']', '}'] 
        if stk.pop() != s[i]:
            return False
        """
        stk = []
        i = 0
        for c in s:
            if c == '(':
                stk.append(')')
            elif c == '{':
                stk.append('}')
            elif c == '[':
                stk.append(']')
            elif not stk or stk.pop() != c:
                return False

        # !stack.isEmpty()
        return not stk 