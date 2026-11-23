class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset= set()
        for i in nums:
            myset.add(i)

        return len(nums) != len(myset)