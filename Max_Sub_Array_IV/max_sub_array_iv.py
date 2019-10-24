# Given an integer arrays, find a contiguous subarray which has the largest sum and length should be greater or equal to given length k.
# Return the largest sum, return 0 if there are fewer than k elements in the array.

# https://www.lintcode.com/problem/maximum-subarray-iv/description


# Input:
# [-2,2,-3,4,-1,2,1,-5,3]
# 5
# Output:
# 5
# Explanation:
# [2,-3,4,-1,2,1]
# sum=5


def maxSubarray4(nums, k):

	length = len(nums)

    if length < k:
        return 0

    # create pre sum list to store all pre sum
    # [0, -2, 0, -3, 1, 0, 2, 3, -2, 1] for input [-2,2,-3,4,-1,2,1,-5,3]
    pre_sum = [0] * (length + 1)
    for i in range(length):
        pre_sum[i+1] = pre_sum[i] + nums[i]
    
    res = 0

    for i in range(k):
        res += nums[i]            
    min_pre_sum = 0

    # get the next res by minus min pre sum
    for i in range(k, length + 1):
        res = max(res, pre_sum[i] - min_pre_sum)
        min_pre_sum = min(min_pre_sum, pre_sum[i - k + 1])
    return res



# this approach is ok when theres no time complexity consideration
# scan the max sum for each index i when i < k
# total time is O(n^2)
from sys import maxsize
def maxSubarray4(nums, k):
    # write your code here
    nums_length = len(nums)
    
    if nums_length < k:
        return 0
        
    result = -maxsize - 1
    for i in range(nums_length -k + 1):
        sum = nums[i]
        min_index = i + k - 1

        for j in range(i + 1, min_index + 1):
            sum += nums[j]
      
        result = max(result, sum)
        print(f'sum is {sum}')
        next_sum = sum
        while min_index + 1 < nums_length:
            min_index += 1
            next_sum += nums[min_index]
            print(f'next sum is {next_sum}')
            result = max(result, next_sum)
            
        print(f'final: {result}')
        
    return result