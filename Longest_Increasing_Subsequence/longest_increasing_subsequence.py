# https://leetcode.com/problems/longest-increasing-subsequence/

# Using idea of dp, create a array to store the max subsequence len at each position.
# And then return the max from the dp array.

def lengthOfLIS(nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        num_len = len(nums)
        dp = [1 for i in range(num_len)]
        
        for i in range(num_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)