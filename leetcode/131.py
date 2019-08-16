def partition(s: str):
    def dfs(string, path, res):
        # 结束条件
        if not string:
            res.append(path)
        for i in range(len(string)):
            # 如果i之前的字段为回文,判断剩下字段能组成回文的可能性
            if string[:i + 1] == string[i::-1]:
                dfs(string[i + 1:], path + [string[:i + 1]], res)

    res, path = [], []
    dfs(s, path, res)
    return res


s = "aab"
print(partition(s))
