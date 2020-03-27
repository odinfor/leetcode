"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""


class Solution:

    def maxAreal1(self, height: list) -> int:
        """暴力破解"""
        max_area = 0
        for i in height:
            for y in height[height.index(i) + 1:]:
                h = i if i < y else y
                w = height.index(y) - height.index(i)

                area = h * w

                if area > max_area:
                    max_area = area
        return max_area

    def maxAreal2(self, height: list) -> int:
        """
        双向指针思想
        从头尾开始,值小的一方向内移动,直到左侧的位置大于等于右侧的位置.
        执行用时：32 ms, 内存消耗：13.4 MB
        """
        x, y = 0, len(height) - 1   # x,y分别为height的头尾索引

        # 首先计算宽度最大的面积
        h = height[x] if height[x] < height[y] else height[y]
        w = y
        max_area = h * w    # 最大面积

        while x < y:
            if height[x] < height[y]:
                x = x + 1
            else:
                y = y - 1

            h = height[x] if height[x] < height[y] else height[y]
            w = y - x
            area = h * w
            max_area = area if area > max_area else max_area

        return max_area


if __name__ == "__main__":
    s = Solution()
    area1 = s.maxAreal2([1,8,6,2,5,4,8,3,7])
    area2 = s.maxAreal2([2, 3, 10, 5, 7, 8, 9])
    print(area1)
    print(area2)
