
public class offer52_正则表达式匹配 {
	public boolean match1(char[] str, char[] pattern) {
        if (str == null || pattern == null) {
            return false;
        }
        return match(str, pattern, 0, 0);
    }

    //match(): 表示s[sIndex~s.length - 1]与 p[pIndex~p.length - 1]是否能匹配得上
    public boolean match(char[] s, char[] p, int sIndex, int pIndex) {
        //p串已经用尽
        if (pIndex == p.length) {
            //若s也已经用尽，则匹配成功，否则，匹配失败
            return sIndex == s.length;
        }
        //pIndex是p最后一个字符，或者 pIndex下一个元素不是'*',则只考虑将s[sIndex]与 p[pIndex]匹配
        if (pIndex + 1 == p.length || p[pIndex + 1] != '*') {
            return sIndex != s.length && (s[sIndex] == p[pIndex] || p[pIndex] == '.') && 
                match(s, p, sIndex + 1, pIndex + 1);
        }
        //若pIndex下一个元素为 *，则需要考虑多个s[sIndex]与 p[pIndex]匹配的情况：枚举
        //例如 a*bb 与 aaaaab这种情况，i会最终停留在b的位置处
        int i = sIndex;
        while (i != s.length && (s[i] == p[pIndex] || p[pIndex] == '.')) {
            if (match(s, p, i + 1, pIndex + 2)) {
                return true;
            }
            i++;
        }
        //match(s, p, sIndex, pIndex + 2) 表示 * 之前的元素为0个，比如 a*aaa 与 aaa 进行匹配
        return match(s, p, sIndex, pIndex + 2);
    }
}
