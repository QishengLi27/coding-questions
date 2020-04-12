# https://leetcode.com/problems/super-egg-drop/


import sys
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        map_dict = {}
        return self.dp(K, N, map_dict)
    
    def dp(self, K, N, map_dict):

        # If only have one egg, test all floors
        if K == 1:
            return N
        # If no floors left, return 0
        if N == 0:
            return 0
        
        # If result already exist, return it
        if (K, N) in map_dict:
            return map_dict[(K, N)]
        
        result = sys.maxsize
        
        # for i in range(1, N+1):
        #     result = min(
        #         result, 
        #         max(
        #             self.dp(K, N - i, map_dict), 
        #             self.dp(K - 1, i - 1, map_dict)
        #         ) + 1
        #     )
        
        left, right = 1, N + 1
        
        while left <= right:
            mid = (left + right) // 2
            broken = self.dp(K - 1, mid - 1, map_dict)
            unbroken = self.dp(K, N - mid, map_dict)
            
            if broken > unbroken:
                right = mid - 1
                result = min(result, broken + 1)
            else:
                left = mid + 1
                result = min(result, unbroken + 1)
        
        map_dict[(K, N)] = result
        return result