class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stk = []
        asteroids.reverse()
        while asteroids:
            if stk == []:
                stk.append(asteroids.pop())

            if asteroids == []:
                return stk

            #print("stk:", stk)
            #print("asteroids:", asteroids)
            former = stk[-1]
            latter = asteroids[-1]

            if former > 0 and latter < 0 and abs(former) > abs(latter):  # boom
                asteroids.pop()
                #print("state1, stk:", stk)
            elif former > 0 and latter < 0 and abs(former) < abs(latter):  # boom
                stk.pop()
                #print("state2, stk:", stk)
            elif former > 0 and latter < 0 and abs(former) == abs(latter):
                stk.pop()
                asteroids.pop()
                #print("state3, stk:", stk)
            else:
                stk.append(asteroids.pop())
                #print("state4, stk:", stk)
        return stk


if __name__ == "__main__":
    test = [
        [5, 10, -5],
        [8, -8],
        [10, 2, -5],
        [3, 5, -6, 2, -1, 4],
        [-2, 2, -1, -2],
        [1, -1, 1, -2]
    ]
    sol = Solution()
    for l in test:
        try:
            result = sol.asteroidCollision(l)
            print(result)
        except Exception as e:
            print("Error:", e)
