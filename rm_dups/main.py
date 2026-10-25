class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        l = []

        for i in s:
            if i not in l:
                l.append(i)
                stack.append(i)
                pass

            elif not stack or (i in l and stack[-1] != i):
                stack.append(i)
                pass

            else:
                stack.pop()

        return "".join(stack)


if __name__ == "__main__":
    solution = Solution()
    strings = [
        "abbaca",
        "azxxzy",
        "aaaaaaaa",
    ]

    for s in strings:
        print(solution.removeDuplicates(s))
