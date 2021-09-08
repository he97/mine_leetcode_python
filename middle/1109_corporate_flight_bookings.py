# 这里有n个航班，它们分别从 1 到 n 进行编号。
#
# 有一份航班预订表bookings ，表中第i条预订记录bookings[i] = [firsti, lasti, seatsi]意味着在从 firsti到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi个座位。
#
# 请你返回一个长度为 n 的数组answer，其中 answer[i] 是航班 i 上预订的座位总数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/corporate-flight-bookings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# 使用差分数组
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        a = [0 for _ in range(n)]
        for i in range(len(bookings)):
            a[bookings[i][0] - 1] += bookings[i][2]
            if bookings[i][1] < n:
                a[bookings[i][1]] -= bookings[i][2]
        b = []
        c = 0
        for i in a:
            c += i
            b.append(c)
        return b
