class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        elementOfS1 = {}
        for i in s1:
            if elementOfS1.get(i):
                elementOfS1[i] += 1
                continue
            elementOfS1[i] = 1
        for left in range(len(s2)):
            if not elementOfS1.get(s2[left]):
                left += 1
                continue
            start = left
            right = start + len(s1)
            if right > len(s2):
                return False
            newElementOfS1 = elementOfS1.copy()
            for i in range(start, right):
                if not newElementOfS1.get(s2[i]):
                    break
                newElementOfS1[s2[i]] -= 1
                if newElementOfS1[s2[i]] == 0:
                    del newElementOfS1[s2[i]]
            if not newElementOfS1:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaoo"))
    print(s.checkInclusion("adc", "dcda"))




