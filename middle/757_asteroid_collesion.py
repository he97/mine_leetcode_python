# 给定一个整数数组 asteroids，表示在同一行的行星。
#
# 对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。
# 每一颗行星以相同的速度移动。
#
# 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。
# 两颗移动方向相同的行星，永远不会发生碰撞。
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []
        for i in range(len(asteroids)):
            if asteroids[i] < 0:
                if len(positive) == 0:
                    result.append(asteroids[i])
                else:
                    tag = False
                    while len(positive) > 0:
                        if positive[-1] < abs(asteroids[i]):
                            positive.pop()
                        elif positive[-1] > abs(asteroids[i]):
                            tag = True
                            break
                        else:
                            tag = True
                            positive.pop()
                            break
                    if not tag:
                        result.append(asteroids[i])
            else:
                positive.append(asteroids[i])
        result.extend(positive)
        return result


demo = Solution()
print(demo.asteroidCollision([-2,-2,1,-2]))
