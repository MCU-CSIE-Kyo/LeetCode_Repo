class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # find max
        max_candies = max(candies)
        ans = []
        for candie in candies:
            greatest = extraCandies + candie
            if greatest > max_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans

