class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for x in s:
            if x in "[{(":
                stack.append(x)
            else:
                if not stack:
                    return False
                
                top = stack.pop()

                if top != pairs[x]:
                    return False
        
        return len(stack) == 0

        