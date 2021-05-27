class Solution:
    def getRow(self, rowIndex: int) -> list:
        if rowIndex == 0:
            return [1]
        begin, curr_line, last_line = [1], [], [1]

        for i in range(rowIndex):
            if i == 0:
                continue
            for x in range(i + 1):
                left, right = x - 1, x
                if left < 0:
                    curr_line.append(1)
                    continue
                if right >= len(last_line):
                    curr_line.append(1)
                    last_line, curr_line = curr_line, last_line
                    
        return last_line
                    

if __name__ == "__main__":
    s = Solution()
    print(s.getRow(5))