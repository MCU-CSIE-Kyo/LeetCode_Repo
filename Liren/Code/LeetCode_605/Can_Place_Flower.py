class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        capability = 0
        border = [0]
        flowerbed.append(0)
        new = border + flowerbed
        for index in range(1, len(new)-1):
            if new[index] == 0 and new[index-1] == 0 and new[index+1] == 0:
                new[index] = 1
                capability += 1
        return capability >= n