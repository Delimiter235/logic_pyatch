class Solution:
    def isValid(self, s: str) -> bool:
        brkts = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for c in s:
            if stack:
                if c != brkts[stack[-1]] and c not in brkts:
                    return not stack
                elif c == brkts[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                if c in list(brkts.values()):
                    return False
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
