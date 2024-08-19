class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            second_element = target - nums[index]
            if second_element in nums[index+1:]:
                second_index = nums[index+1:].index(second_element) + index + 1
                return [index, second_index]