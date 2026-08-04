class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            temp = nums[i]
            nums.pop(i)
            mult = math.prod(nums)
            ans.append(mult)
            nums.insert(i, temp)
        return ans
