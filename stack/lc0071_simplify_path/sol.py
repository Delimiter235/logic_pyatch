class Solution:
    def simplifyPath(self, path: str) -> str:
        stack: list = []
        string: str = ""
        for c in path + "/":
            if c == "/":
                if string in (".", ""):
                    #print(1)
                    string = ""
                    continue
                elif string == "..":
                    try:
                        stack.pop()
                    except Exception as e:
                        string = ""
                        continue
                else:
                    stack.append(string)
                string = ""
            else:
                string += c
            #print(string)
        #print(stack)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    test = [
        #"/home/",
        #"/home//foo/",
        #"/home/./foo/",
        #"/home/user/Documents/../Pictures",
        #"/../",
        #"/.../a/../b/c/../d/./",
        "/a/../../c"
        #"/a/../../b/../c//.//",
    ]
    for t in test:
        try:
            print(sol.simplifyPath(t))
        except Exception as e:
            print("Error:", e)
