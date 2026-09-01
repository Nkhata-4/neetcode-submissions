class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr) - 1):
            remain = arr[i+1:len(arr)]
            ans.append(max(remain))
        ans.append(-1)
        return ans
            