class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        stk1 = []
        stk2 = []
        brackets = ["[", "]"]
        loop_count = 0
        for char in s:  # "]"
            #print("Loop:", loop_count)
            stk.append(char)  # e.g. stk = ["3", "[", "a", "2", "[", "c", "]"]
            #print("stk_s1:", stk)
            if char == brackets[1]:  # stk[-1] == "]"
                stk.pop()  # pop "]"
                #print("stk_s2:", stk)
                while stk[-1] != brackets[0]:  # "["
                    # stk1 = ["c"], stk = ["3", "[", "a", "2", "["]
                    stk1.append(stk.pop())
                #print("stk_s3:", stk)
                #print("stk1_s1:", stk1)
                stk.pop()  # pop "[" from stk, stk = ["3", "[", "a", "2"]
                #print("stk_s4:", stk)
                while stk and stk[-1] not in brackets:  # e.g. browse "a" and "2"
                    if stk[-1].isdigit(): # "2"
                        stk2.append(stk.pop())  # stk2 = ["2"]
                    else:  # "a"
                        break
                #print("stk_s5:", stk)
                #print("stk2_s1:", stk2)
                stk1.reverse()
                stk2.reverse()
                x = int("".join(stk2))  # "2"
                #print(x)
                y = x * "".join(stk1)  # "cc"
                #print(y)
                stk.append(y)  # stk = ["3", "[", "a", "cc"]
                #print("stk_s6:", stk)
                stk1 = []
                stk2 = []
            loop_count += 1
        return "".join(stk)


if __name__ == "__main__":
    test = [
        "3[a]2[bc]",
        "3[a2[c]]",
        "2[abc]3[cd]ef",
        "abc3[cd]xyz",
    ]
    sol = Solution()
    for s in test:
        try:
            result = sol.decodeString(s)
            print(result)
        except Exception as e:
            print("Error:", e)
