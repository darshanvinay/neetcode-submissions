class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=0
        for i in range(len(nums)):
            if nums[i] == target:
                a=i
            
        if nums[a] != target:
            return -1
        else:
            return a

        