def wordBreak(s, wordDict) -> bool:
    # 该方法会超时
    # if not s: return True
    # n = len(s)
    # for i in range(n):
    #     if s[:i + 1] in wordDict and self.wordBreak(s[i + 1:], wordDict):
    #         return True
    # return False

    import functools
    wordDict = set(wordDict)
    if not wordDict: return not s
    # 找最长单词的长度
    max_len = max(map(len, wordDict))

    @functools.lru_cache(None)
    def helper(s):
        # 递归终止条件
        if not s: return True
        for i in range(len(s)):
            # 判断是否满足条件，如果i比最大的单词还要长，说明前面的部分已经失败了，优化了时间
            if i < max_len and s[:i + 1] in wordDict and helper(s[i + 1:]):
                return True
        return False

    return helper(s)


s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]
print(wordBreak(s, wordDict))
