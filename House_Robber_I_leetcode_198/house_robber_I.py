class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)

        # create a list to store the largest amount for each position
        dp_map = [-1 for i in range(l)]

        # call dp
        return self.dp(nums, 0, dp_map)
    
    def dp(self, nums, start, dp_map):

        # if we hit the end, return 0
        if start >= len(nums):
            return 0
        
        # check if we already have the amount for current position
        if dp_map[start] != -1:
            return dp_map[start]
        
        # get the max number from two cases:
        # I: dont rob, go to next house
        # II: rob current house, go to +2 position
        result = max(
            self.dp(nums, start+1, dp_map),
            nums[start] + self.dp(nums, start+2, dp_map)
        )
        
        # store result in the map
        dp_map[start] = result
        
        return result