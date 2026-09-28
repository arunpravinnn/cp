class Solution:
    def maxDepth(self, s: str) -> int:
        depths = []
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                count -= 1
            depths.append(count)
        return max(depths)
            
        