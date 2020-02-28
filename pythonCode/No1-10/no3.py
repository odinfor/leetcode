"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例1
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例2
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例3
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:

    @staticmethod
    def length1(s: str) -> int:
        str1 = []
        for i in range(len(s)):
            str2, y = [], i
            str2.append(s[i])

            while 1:
                y += 1
                if y >= len(s) or s[y] in str2:
                    break
                if s[y] not in str2:
                    str2.append(s[y])
            if len(str2) > len(str1):
                str1 = str2
        print("".join(str1))
        return len(str1)

    @staticmethod
    def length2(s: str) -> int:
        # 滑动窗口思想解法
        # 1.左侧索引和右侧索引均为0开始,左侧索引不动,右侧索引自增扩大窗口,直到右侧索引值在窗口内出现重复.
        # 2.左侧窗口右移一位,右侧索引值是否重复.重复左侧窗口继续右移.
        # 3.重复上述过程直到右侧索引到最后.
        if not s:
            return 0

            # 保存窗口内字符串
            lookup = []
            n = len(s)
            # 最大子串长度
            max_len = 0
            # 当前窗口长度
            cur_len = 0
            # 遍历字符串s
            for i in range(n):
                val = s[i]
                # 如果该值不在窗口中
                if val not in lookup:
                    # 添加到窗口内
                    lookup.append(val)
                    # 当前长度+1
                    cur_len += 1
                # 如果该值在窗口中已存在
                else:
                    # 获取其在窗口中的位置
                    index = lookup.index(val)
                    # 移除该位置及之前的字符，相当于上图中的图3到图4
                    lookup = lookup[index+1:]
                    lookup.append(val)
                    # 当前长度更新为窗口长度
                    cur_len = len(lookup)
                # 如果当前长度大于最大长度，更新最大长度值
                max_len = cur_len if cur_len > max_len else max_len
            # 返回最大子串长度
            return max_len






if __name__ == "__main__":
    s = Solution()
    print(s.length1("abcabcbb"))
    print(s.length1("bbbbb"))
    print(s.length1("pwwkew"))

    print(s.length2("abcabcbb"))
    print(s.length2("bbbbb"))
    print(s.length2("abcabcbb"))