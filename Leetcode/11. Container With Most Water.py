class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height) - 1

        while right > left:
            space = right - left

            if height[left] <= height[right]:
                cur_area = space * height[left]
                max_area = cur_area if cur_area > max_area else max_area
                left += 1
            else:
                cur_area = space * height[right]
                max_area = cur_area if cur_area > max_area else max_area
                right -= 1
        return max_area