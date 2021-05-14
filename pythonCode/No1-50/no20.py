"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
输入: "()"
输出: true

输入: "()[]{}"
输出: true

输入: "(]"
输出: false

输入: "([)]"
输出: false

输入: "{[]}"
输出: true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        """使用栈,最后的栈为空则为有效"""
        stack = []
        dict1 = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if not stack and i in dict1:
                stack.append(i)
            elif stack and dict1.get(stack[-1]) and dict1.get(stack[-1]) != i:
                stack.append(i)
            elif stack and dict1.get(stack[-1]) and dict1.get(stack[-1]) == i:
                stack.pop(len(stack) - 1)
            else:
                return False
        return False if stack else True


if __name__ == "__main__":
    run = Solution()
    # print(run.isValid("()"))
    # print(run.isValid("()[]{}"))
    # print(run.isValid("(]"))
    # print(run.isValid("([)]"))
    # print(run.isValid("{[]}"))
    # print(run.isValid("({[]}())"))
    # print(run.isValid("([)"))
    print(run.isValid(")"))


