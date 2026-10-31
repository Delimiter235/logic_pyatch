class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()

            else:
                stack.append(c)

        return "".join(stack)


if __name__ == "__main__":
    solution = Solution()
    strings = [
        "abbaca",
        "azxxzy",
        "aaaaaaaa",
    ]

    for s in strings:
        try:
            print(solution.removeDuplicates(s))
        except Exception as e:
            print("Eorror:", e)
