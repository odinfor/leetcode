class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        if sum(gas) < sum(cost):
            return -1
        sumLeft = 0
        currNode = 0
        while currNode < len(gas):
            if gas[currNode] - cost[currNode] >= 0:
                startIdx = currNode
                sumRight = 0
                # 计算按照该节点往下走的剩余油量
                for i in range(startIdx, len(gas)):
                    sumRight += gas[i] - cost[i]
                    if sumRight < 0:
                        currNode = i + 1
                        break
                if sumRight >= 0 and sumRight + sumLeft >= 0:
                    return startIdx
            else:
                sumLeft += gas[currNode] - cost[currNode]
                currNode += 1

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(s.canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6]))