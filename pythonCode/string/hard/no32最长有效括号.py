class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        ans, em = 0, {"(": 1, ")": -1}
        left = 0

        while left < len(s):
            currNum = 0
            if em[s[left]] != 1:
                left += 1
                continue
            right = left + 1
            while left < len(s) and right < len(s):
                if em[s[left]] + em[s[right]] == 0:
                    currNum += 1
                    left += 2
                    continue
                else:
                    ans = max(ans, currNum)
                    left += 1

        return ans * 2


if __name__ == "__main__":
    print(Solution().longestValidParentheses(")()())"))
                     
