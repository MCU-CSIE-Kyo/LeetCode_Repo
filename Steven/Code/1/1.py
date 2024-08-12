class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []
        
        for index in range(len(nums)):
            for i in range(index+1, len(nums)):
                if nums[index] + nums[i] == target:
                    ans.append(index)
                    ans.append(i)
        return ans