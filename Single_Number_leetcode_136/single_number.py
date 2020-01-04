# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Input: [4,1,2,1,2]
# Output: 4

# using XOR, a list of numns become a1^a2^a1^a3^a1, which is (a1^a1)^(a2^a2)^a3
def singleNumber(nums: List[int]) -> int:
	result = 0
		for num in nums:
			result ^=num
	return result