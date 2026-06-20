class Solution:
    
    
    class Trie:
        class TrieNode:
            def __init__(self, c):
                self.val = c
                self.children = [None] * 26
                self.end = False
        
        def __init__(self):
            self.root = self.TrieNode('-1')

        def insert(self, word):
            node = self.root
            for c in word:
                i = ord(c) - ord('a')
                if not node.children[i]:
                    node.children[i] = self.TrieNode(c)
                node = node.children[i]
            node.end = True
            return

        def search(self, word): 
            node = self.root
            for c in word:
                i = ord(c) - ord('a')
                if not node.children[i]:
                    return False
                node = node.children[i]
            return True if node.end else False

        def startswith(self, word): 
            node = self.root
            for c in word:
                i = ord(c) - ord('a')
                if not node.children[i]:
                    return False
                node = node.children[i]
            return True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # local visited matrice m*n space
        trie = self.Trie()
        for word in words:
            trie.insert(word)
        res = set()
        def dfs(i, j, visited, word):
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
                return False
            if (i, j) in visited:
                return False
            word += board[i][j]
            if not trie.startswith(word):
                return False
            if trie.search(word) == True:
                res.add(word)

            visited.add((i,j))
            
            for x,y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                dfs(i+x, j+y, visited, word)
            visited.remove((i,j))
            
        for m in range(len(board)):
            for n in range(len(board[0])):
                dfs(m, n, set(), "")
        
        return list(res)
        
        

            

        


        