from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators_to_foo = {
            "+": lambda a, b: int(a+b),
            "-": lambda a, b: int(a-b),
            "*": lambda a, b: int(a*b),
            "/": lambda a, b: int(a/b),
        }
        stk = list()
        for t in tokens:
            num = t
            try:
                num = int(t)
            except ValueError:
                num1 = stk.pop()
                num2 = stk.pop()
                num = operators_to_foo[t](num2, num1)
            finally:
                stk.append(num)

        return stk[0]


if __name__ == "__main__":
    solution = Solution()
    token_lists = [
        ["2","1","+","3","*"],
        ["4","13","5","/","+"],
        ["0","3","/"],
    ]
    for tokens in token_lists:
        print(solution.evalRPN(tokens))

