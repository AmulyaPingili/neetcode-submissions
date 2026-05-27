class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #approach 1 set
        setn = len(set(nums))
        numsn = len(nums)
        return setn!=numsn