"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 12
"""
import math


class Solution:

    def __is_int32(self, x: int) -> bool:
        min, max = -math.pow(2, 32) + 1, math.pow(2, 32)

        return True if min <= x <= max else False

    # 执行时间60ms,内存消耗13.3MB
    def reverse1(self, x: int) -> int:
        if x == 0:
            return x
        elif not self.__is_int32(x):
            return 0

        b = abs(x)
        while 1:
            if b % 10:
                break
            else:
                b = int(b / 10)

        c = str(b)
        c = int(c[::-1])

        # int32范围判断
        if x > 0:
            return c if c < math.pow(2, 32) else 0
        else:
            return -c if c > math.pow(2, 32) + 1 else 0


if __name__ == "__main__":
    s = Solution()
    print(s.reverse1(131))
    print(s.reverse1(-123))
    print(s.reverse1(120))
    print(s.reverse1(1534236469))
    print(s.reverse1(-2147483648))
    print(s.reverse1(-1563847412))

    print(int(math.pow(2, 31)), 0 - int(math.pow(2, 31)))




