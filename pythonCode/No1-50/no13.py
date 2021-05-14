"""
同no12.py中描述,将输入的罗马数字转为数字
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""


class Solution:

    def romanToInt(self, s: str) -> int:
        """
        观察罗马数字字符串,对比两个字符串,左边大于右边相加,左边小于右边减掉即可。
        """
        hashmap = {
            "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
        }
        rst = 0

        for index in range(len(s) - 1):     # 避免index+1索引越界,只遍历到倒数第二位,return时需要加上最后一位的结果
            if hashmap[s[index]] < hashmap[s[index + 1]]:
                rst -= hashmap[s[index]]
            else:
                rst += hashmap[s[index]]

        return rst + hashmap[s[-1]]


if __name__ == "__main__":
    run = Solution()
    print(run.romanToInt("MCMXCIV"))
