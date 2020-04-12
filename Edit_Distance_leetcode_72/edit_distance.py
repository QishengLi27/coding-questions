# https://leetcode.com/problems/edit-distance/


# Using two pointers, compare two strings from end to start.
#example: "horse", "ros"
# One approach:
# 1. horss, ros :replace
# 2. horos, ros :replace
# 3. oros, ros :delete
# 4. ros, ros :delete
# Or
# 1. hors, ros :delete
# 2. hoos, ros :replace
# 3. hros, ros :replace
# 4. ros, ros :delete

# The idea is that if value is the same, each pointer moves to the left one step,
# else we do insert/delete/replace and get the min steps from those three.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dpDict = {}
        return self.dp(word1, word2, len(word1)-1, len(word2)-1, dpDict)
    
    def dp(self, word1, word2, i, j, dpDict):
        if (i, j) in dpDict:
            return dpDict[(i, j)]
        
        if i == -1: 
            return j + 1
        if j == -1: 
            return i + 1
        
        if word1[i] == word2[j]:
            dpDict[(i, j)] = self.dp(word1, word2, i-1, j-1, dpDict)
        else:
            dpDict[(i, j)] = min(
                # insert: insert the char at current position, so that first pointer dont move
                self.dp(word1, word2, i, j - 1, dpDict) + 1,

                #delete: delete current char for word1, so first pointer move
                self.dp(word1, word2, i - 1, j, dpDict) + 1,

                # replace: replace char at current position for word1, both pointer move
                self.dp(word1, word2, i - 1, j - 1, dpDict) + 1 #replace
            )
        
        return dpDict[(i, j)]