class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = {}

        start, end = 0, len(nums) - 1

        while start <= end:

            if end != start and nums[start] == nums[end]:
                return True

            if nums[start] in seen or nums[end] in seen:
                return True
            
            seen[nums[start]] = nums[start]
            seen[nums[end]] = nums[end]
            start += 1
            end -= 1

        return False
            
        