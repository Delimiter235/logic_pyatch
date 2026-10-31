class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack


if __name__ == "__main__":
    sol = Solution()
    tests = [
        "()",
        "()[]{}",
        "(]",
        "([])",
        "([)]",
        "){",
    ]
    for s in tests:
        try:
            print(sol.isValid(s))
        except Exception as e:
            print(e)
