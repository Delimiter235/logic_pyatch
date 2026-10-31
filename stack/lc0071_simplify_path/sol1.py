class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path.split("/"):
            if s in  (".", ""):
               continue
            elif s == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(s)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()
    test = [
        "/home/",
        "/home//foo/",
        "/home/./foo/",
        "/home/user/Documents/../Pictures",
        "/../",
        "/.../a/../b/c/../d/./",
        "/a/../../c"
        "/a/../../b/../c//.//",
    ]
    for t in test:
        try:
            print(sol.simplifyPath(t))
        except Exception as e:
            print("Error:", e)
