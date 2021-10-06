# 给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。
#
# 每个矩形由其 左下 顶点和 右上 顶点坐标表示：
#
# 第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
# 第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rectangle-area
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import dis


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        width_1 = ax2 - ax1
        height_1 = ay2 - ay1
        width_2 = bx2 - bx1
        height_2 = by2 - by1
        s1 = width_1 * height_1
        s2 = width_2 * height_2
        """
        判断有没有相交的地方,以一个矩形固定
        """
        if bx1 >= ax2 or by1 >= ay2 or by2 <= ay1 or bx2 <= ax1:
            return s1 + s2
        height_3 = width_3 = 0
        if ax1 <= bx1 <= ax2 <= bx2:
            width_3 = ax2 - bx1
        elif ax1 <= bx1 <= bx2 <= ax2:
            width_3 = width_2
        elif bx1 <= ax1 <= ax2 <= bx2:
            width_3 = width_1
        elif bx1 <= ax1 <= bx2 <= ax2:
            width_3 = bx2 - ax1
        if by1 <= ay1 <= ay2 <= by2:
            height_3 = height_1
        elif ay1 <= by1 <= by2 <= ay2:
            height_3 = height_2
        elif by1 <= ay1 <= by2 <= ay2:
            height_3 = by2 - ay1
        elif ay1 <= by1 <= ay2 <= by2:
            height_3 = ay2 - by1
        s3 = height_3 * width_3
        return s1 + s2 - s3



demo = Solution()
print(demo.computeArea(-2
,-2
,2
,2
,-3
,1
,-1
,3))
print(demo.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))
print(demo.computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2))