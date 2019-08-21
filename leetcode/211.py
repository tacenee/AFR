


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.set_map = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.set_map
        for c in word:
            tree = tree.setdefault(c, {})
        tree['#'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def helper(word, tree):
            if not word:
                if '#' in tree:
                    return True
                return False
            if word[0] == '.':
                for i in tree:
                    if helper(word[1:], tree[i]):
                        return True
            elif word[0] in tree:
                if helper(word[1:], tree[word[0]]):
                    return True
            return False

        return helper(word, self.set_map)
