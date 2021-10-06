# 给定一个整数数组prices，其中第i个元素代表了第i天的股票价格 ；整数fee 代表了交易股票的手续费用。
# 
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 
# 返回获得利润的最大值。
# 
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        low = high = prices[0]
        count = 0
        buy = False
        tag = True
        n = len(prices)
        i = 0
        while i < n:
            # 是不是一个新的购买周期
            if tag:
                low = high = prices[i]
                tag = False
            else:
                # 有没有购入股票
                if not buy:
                    if prices[i] < low:
                        low = prices[i]
                    if prices[i] >= low + fee:
                        high = prices[i]
                        buy = True
                else:
                    if prices[i] > high:
                        high = prices[i]
                    elif prices[i] <= high - fee:
                        count += high - low - fee
                        tag = True
                        buy = False
                        continue
            i += 1
        if buy:
            count += high - low - fee
        return count

demo = Solution()
print(demo.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2))



