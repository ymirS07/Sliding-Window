class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        num_map = Counter()
        for right, x in enumerate(nums):
            num_map[x] += 1
            while num_map[x] > k:
                
                num_map[nums[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
               


        return max_len
