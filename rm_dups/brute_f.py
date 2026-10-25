class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in s:
            if not stack:
                stack.append(i)

            elif stack[-1] != i:
                stack.append(i)
            
            else:
                stack.pop()

        return "".join(stack)


if __name__ == "__main__":
    solution = Solution()
    strings = [
        "abbaca",
        "azxxzy",
        "aaaaaaaa",
        "abbbabaaa",
    ]

    for s in strings:
        print(solution.removeDuplicates(s))
