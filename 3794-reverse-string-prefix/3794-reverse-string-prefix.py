class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        stack = []
        for i in range(k):
            stack.append(s[i])
        answer = ""
        for i in range(k):
            answer+= stack.pop()
        answer += s[k:]

        return answer

        