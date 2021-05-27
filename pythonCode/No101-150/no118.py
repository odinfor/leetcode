class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        begin, result_list = [1], []

        for i in range(numRows):
            last = []
            if i == 0:
                result_list.append(begin)
                continue
            for x in range(i + 1):
                left, right = x - 1, x
                if left < 0:
                    last.append(1)
                    continue
                if right >= len(result_list[-1]):
                    last.append(1)
                    result_list.append(last)
                    break
                last.append(result_list[-1][left] + result_list[-1][right])

        return result_list


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))

