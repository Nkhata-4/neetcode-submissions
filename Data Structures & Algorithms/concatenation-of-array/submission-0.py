class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        '''for i in range(len(nums)):
            k = nums[i]
            ans = ans.append(k)'''
        return ans * 2