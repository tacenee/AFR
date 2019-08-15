from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        l = len(beginWord)
        word_dict = {}
        for word in wordList:
            for i in range(l):
                # word_dict[word[:i] + '_' + word[i + 1:]].append(word)
                tmp = word[:i] + "_" + word[i + 1:]
                word_dict[tmp] = word_dict.get(tmp, []) + [word]

        queue = [(beginWord, 1)]
        visit = {beginWord: True}
        while queue:
            cur_word, level = queue.pop(0)
            for i in range(l):
                #python3之前的版本会因为元组报错
                current = cur_word[:i] + "_" + cur_word[i + 1:]
                word_list = word_dict.get(current, [])
                for word in word_list:
                    if word == endWord:
                        return level + 1
                    if word not in visit:
                        visit[word] = True
                        queue.append((word, level + 1))
                # 删除用过的字典内容
                word_dict[current] = []
        return 0
