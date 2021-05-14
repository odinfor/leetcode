class Solution:
    """
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
    示例
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
    """
    def __is_palindrome(self, s: str) -> bool:
        # 校验字符串是否为回文
        return True if s == s[::-1] else False

    def __get_palindrome(self, s: str) -> list:
        # 生成回文
        str1 = s + s[::-1]      # baab形式的回文
        str2 = s + s[:-1][::-1]    # bab形式的回文
        return [str1, str2]

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
        """
        i, j = left, right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1

    # 暴力破解,超出时间限制
    def max_len_palindrome1(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        max_palindrome = ""
        for i in range(len(s)):
            y = i + 1
            while y <= len(s):
                str1 = s[i: y]
                if self.__is_palindrome(str1) and len(str1) > len(max_palindrome):    # 保存当前最长的回文串
                    max_palindrome = str1
                y += 1

        return max_palindrome

    # 优化解法,逆向生成str的回文,超出时间限制
    def max_len_palindrome2(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        max_palindrome = ""

        for i in range(len(s)):
            y = i + 1
            while y <= len(s):
                str1 = s[i:y]
                if len(s) < len(str1) * 2 - 1:  # 回文长度最大为2n-1
                    break
                palindromes = self.__get_palindrome(str1)
                for palindrome in palindromes:
                    if palindrome in s and len(palindrome) > len(max_palindrome):
                        max_palindrome = palindrome
                y += 1

        return max_palindrome

    # 中心扩散方法,执行用时:1720 ms,内存消耗:13.6MB
    def max_len_palindrome3(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        max_len = 1     # 至少是 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even    # 当前找到的最长回文子串

            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.max_len_palindrome1("babad"))
    print(s.max_len_palindrome1("bb"))

    print(s.max_len_palindrome2("babad"))
    print(s.max_len_palindrome2("bb"))

    print(s.max_len_palindrome3("babad"))
    print(s.max_len_palindrome3("bb"))
