"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
示例 :
输入: s = "anagram", t = "nagaram"
输出: true
输入: s = "rat", t = "car"
输出: false
"""

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        """通过dict形式"""
        dict_s, dict_t = {}, {}
        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1

        for i in t:
            if i not in dict_t:
                dict_t[i] = 1
            else:
                dict_t[i] += 1

        return True if dict_s == dict_t else False

    def isAnagram2(self, s: str, t: str) -> bool:
        """通过dict形式，优化只需要一个dict"""
        dict_str = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dict_str[s[i]] = dict_str[s[i]] + 1 if dict_str.get(s[i]) else 1
            dict_str[t[i]] = dict_str[t[i]] - 1 if dict_str.get(t[i]) else -1

        for _, v in dict_str.items():
            if v != 0:
                return False
        return True



if __name__ == "__main__":
    run = Solution()
    print(run.isAnagram1("anagram", "nagaram"))
    print(run.isAnagram1("rat", "car"))

    print(run.isAnagram2("anagram", "nagaram"))
    print(run.isAnagram2("rat", "car"))