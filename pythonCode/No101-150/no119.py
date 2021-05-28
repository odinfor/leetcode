class Solution:
    def getRow(self, rowIndex: int) -> list:
        if rowIndex == 0:
            return [1]

        begin = [1] # 第一层起始值，作为循环开始的上一个节点
        # 从第二层开始计算, 计算到下一层，返回begin，由于rowIndex是索引值，所以range到rowIndex+2
        for i in range(2, rowIndex + 2):
            result_list = []
            for x in range(i):
                left, right = x - 1, x
                if left < 0:
                    result_list.append(1)
                    continue
                if right >= i - 1:
                    result_list.append(1)
                    begin = result_list
                    break
                result_list.append(begin[left] + begin[right])
                
        return begin
                    

if __name__ == "__main__":
    s = Solution()
    print(s.getRow(5))
