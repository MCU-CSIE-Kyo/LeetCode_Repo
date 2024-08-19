class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        for index in candies:
            if (index + extraCandies) >= max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans