class Solution:
    def replaceWords(self, dictionary: list, sentence: str) -> str:

        dMap, maxRootLen = dict(), 0
        resList, senList = list(), sentence.split(" ")

        for i in dictionary:
            dMap[i] = len(i)
            maxRootLen = max(maxRootLen, len(i))

        for subSentence in senList:
            if len(subSentence) <= 1:
                resList.append(subSentence)
                continue
            left, right = 0, 1
            while right < len(subSentence):
                if not dMap.get(subSentence[left: right]):
                    right += 1
                    if right == len(subSentence):
                        resList.append(subSentence)
                        break
                    continue
                resList.append(subSentence[left: right])
                break
        
        return " ".join(resList)


if __name__ == "__main__":
    print(Solution().replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
    # print(Solution().replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))