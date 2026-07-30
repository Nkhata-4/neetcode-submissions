class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mylist = []
        while k > 0:
            most = 0
            element = None
            for i in range(len(nums)):
                count = nums.count(nums[i])
                if count > most:
                    most = count
                    element = nums[i]
            mylist.append(element)
            nums = [x for x in nums if x != element]
            k -= 1
        return mylist
