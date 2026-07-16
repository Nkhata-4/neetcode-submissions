class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in operations:
            match i:
                case "+":
                    j = ans[-1] + ans[-2]
                    ans.append(j)
                case "D":
                    k = ans[-1] * 2
                    ans.append(k)
                case "C":
                    ans.pop()
                case _:
                    ans.append(int(i))
        return sum(ans)


