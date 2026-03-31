class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stk = []
        for a in asteroids:
            while stk and stk[-1] > 0 and a < 0:
                if stk[-1] < -a:
                    stk.pop()
                elif stk[-1] == -a: # -a is for absolute value so if value is (-8) it will be 8
                    stk.pop()
                    break
                else:
                    break
            else:
                stk.append(a)
        return stk
        # O(n) -> all operations + iterating through all aesteroids
        # O(n) -> no collision and all aesteroids in the stack