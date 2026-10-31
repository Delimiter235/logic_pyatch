from typing import List, Tuple


class Solution:
    def runLenDecode(self, s: str) -> str:
        stack: List[Tuple[int, str]] = []
        cnt_fld: int = 0
        data_fld: str = ""
        for c in s:
            if c == "[":
                stack.append((cnt_fld, data_fld))
                cnt_fld, data_fld = 0, ""
            elif c == "]":
                cur_cnt, prev_data = stack.pop()
                data_fld = prev_data + cur_cnt * data_fld
            elif "0" <= c <= "9":
                cnt_fld = 10 * cnt_fld + int(c)
            else:
                data_fld += c
        return data_fld


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
            result = sol.runLenDecode(s)
            print(result)
        except Exception as e:
            print("Error:", e)
