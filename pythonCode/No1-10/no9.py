"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
输入: 121
输出: true
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        """
        思路一: 将中卫数左右两边的其中一边进行反转得到一样的即为True
        执行用时 :100 ms, 在所有 Python3 提交中击败了23.92%的用户,内存消耗 :13.5 MB, 在所有 Python3 提交中击败了6.70%的用户
        """
        if x < 0:
            return False
        elif 0 < x < 10:
            return True

        x_list = list(str(x))

        if len(x_list) % 2 == 1:    # 长度为奇数,则中位两端需相反
            middle_index = len(x_list) // 2
            l_list, r_list = x_list[: middle_index], x_list[middle_index + 1:]

            return True if l_list == r_list[::-1] else False
        else:       # 偶数
            middle_index = len(x_list) // 2
            l_list, r_list = x_list[: middle_index], x_list[middle_index:]

            return True if l_list == r_list[::-1] else False

    def isPalindrome2(self, x: int) -> bool:
        """
        思路同上,改变方法用来减少内存空间消耗.
        每次%10求余,每次余数*10相加即能得到反转的效果.直到原数小于或等于反转的数即为到达中卫数
        """
        if x < 0:
            return False
        elif 0 <= x < 10:
            return True
        elif x > 0 and x % 10 == 0:
            return False
        l_num, r_num = x, 0
        while 1:
            r_num = r_num * 10 + l_num % 10
            l_num = l_num // 10
            if r_num == l_num:
                return True if r_num == l_num else False
            elif r_num > l_num:
                return True if r_num // 10 == l_num else False

    def isPalindrome3(self, x: int) -> bool:
        """
        执行用时72ms,内存消耗13.4MB
        :param x:
        :return:
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        else:
            reverse_x = 0
            while x > reverse_x:
                remainder = x % 10
                reverse_x = reverse_x * 10 + remainder
                x = x // 10
            # 当x为奇数时, 只要满足 reverse_x//10 == x 即可
            if reverse_x == x or reverse_x // 10 == x:
                return True
            else:
                return False


if __name__ == "__main__":
    run = Solution()
    # print(run.isPalindrome2(11))
    # print(run.isPalindrome2(12321))
    # print(run.isPalindrome2(1221))

    print(run.isPalindrome3(11))
    print(run.isPalindrome3(12321))
    print(run.isPalindrome3(1221))