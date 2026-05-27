class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in dict1:
                return [dict1[nums[i]],i]
            dict1[target-nums[i]] = i
