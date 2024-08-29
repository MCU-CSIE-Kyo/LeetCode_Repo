class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lengthOfList = len(nums)
        for x in range(lengthOfList):
            for y in range(x+1,lengthOfList):
                if nums[x]+nums[y] == target:
                    return [x,y]
