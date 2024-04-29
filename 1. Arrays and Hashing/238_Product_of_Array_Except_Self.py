class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        # product, zero_count = 1, 0

        # for i in nums:
        #     if i != 0:
        #         product *= i
        #     else:
        #         zero_count += 1

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         if zero_count > 1:
        #             nums[i] = 0
        #         else:
        #             nums[i] = product
        #     else:
        #         if zero_count > 0:
        #             nums[i] = 0
        #         else:
        #             nums[i] = product // nums[i]

        # return nums