class PrefixTree:

    class TrieNode:
        def __init__(self, c):
            self.val = c
            self.mp = [None for i in range(26)] 
            self.end = False
        
    def __init__(self):
        self.root = self.TrieNode('-1')

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            # insert: apple 
            # create a TrieNode if we do not see it in the map
            idx = ord(c)-ord('a')
            if not node.mp[idx]:
                node.mp[idx] = self.TrieNode(c)
             # we have the node in the map, so traverse down the trie
            node = node.mp[idx]
        node.end = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if not node.mp[idx]:
                return False
            node = node.mp[idx]
        
        return True if node.end else False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            idx = ord(c)-ord('a')
            if not node.mp[idx]:
                return False
            node = node.mp[idx]
        return True
        
        