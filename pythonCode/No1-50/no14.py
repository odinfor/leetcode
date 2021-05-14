"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例：
输入: ["flower","flow","flight"]
输出: "fl"
输入: ["dog","racecar","car"]
输出: ""
"""


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        """
        第一和第二个元素的公共部分遍历查找
        执行用时76 ms
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        start, max_head, index = strs[0], "", 0

        for index in range(min(len(start), len(strs[1]))):
            if start[index] == strs[1][index]:
                max_head += start[index]
            else:
                break

        for i in strs[2:]:
            head = ""
            for index in range(min(len(max_head), len(i))):
                if max_head[index] == i[index]:
                    head += start[index]
                else:
                    break
            if head == "":
                max_head = ""
                break
            max_head = head if len(head) < len(max_head) else max_head

        return max_head


if __name__ == "__main__":
    run = Solution()
    print(run.longestCommonPrefix(["flower","flow","flight"]))


