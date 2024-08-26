class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for number in candies:
            kid = number + extraCandies
            if kid >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result