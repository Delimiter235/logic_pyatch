from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = [
            "+", "-",
            "*", "/",
        ]
        for t in tokens:
            if t == "/" and stk[-1] == "0":
                return False

            if t in operators and len(stk) < 2:
                return False
           
            if t in operators and len(stk) >= 2:
                num1 = stk.pop()
                num2 = stk.pop()
                res = int(eval(num2+t+num1))
                stk.append(str(res))

            elif isinstance(int(t), int):
                stk.append(t)

            else:
                return False

        return int(stk[0])


if __name__ == "__main__":
    solution = Solution()
    token_lists = [
        #["2","1","+","3","*"],
        #["4","13","5","/","+"],
        ["0","3","/"],
    ]
    for tokens in token_lists:
        print(solution.evalRPN(tokens))
        
