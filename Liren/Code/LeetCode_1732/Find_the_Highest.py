class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        new_list = []
        address = 0
        for index in gain:
            address += index
            new_list.append(address)
        new_list = [0] + new_list
        return max(new_list)