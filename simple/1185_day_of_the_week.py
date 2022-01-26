# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
# 输入为三个整数：day、month 和 year，分别表示日、月、年。
#
# 您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/day-of-the-week
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
思路就是调用库函数
"""
import calendar


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        a = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
        return a[calendar.weekday(day=day, month=month, year=year)]
