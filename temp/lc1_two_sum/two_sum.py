class Solution:
    def two_sum_hash(self, nums: list, target: int) -> list:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []
    
    def two_sum_for_loop(self, nums: list, target: int) ->list:
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def two_sum_while_loop(self, nums: list, target: int) ->list:
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
