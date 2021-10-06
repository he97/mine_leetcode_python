from collections import defaultdict


class DetectSquares(object):

    def __init__(self):
        self.d = {}
        # self.d = [defaultdict(int) for _ in range(1001)]

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        # self.d[point[0]][point[1]] += 1
        if point[0] not in self.d.keys():
            d = {point[1]: 1}
            self.d[point[0]] = d
        else:
            if point[1] not in self.d[point[0]].keys():
                self.d[point[0]][point[1]] = 1
            else:
                self.d[point[0]][point[1]] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        count = 0
        if point[0] not in self.d.keys():
            return 0
        for x in self.d[point[0]].keys():
            if x < point[1]:
                edge = point[1] - x
                a = self.d[point[0]][x]
                if point[0] - edge in self.d.keys() and point[1] - edge in self.d[point[0] - edge].keys() and point[1] in self.d[point[0] - edge].keys():
                    count += a * self.d[point[0] - edge][point[1] - edge] * self.d[point[0] - edge][point[1]]
                if point[0] + edge in self.d.keys() and point[1] - edge in self.d[point[0] + edge].keys() and point[1] in self.d[point[0] + edge].keys():
                    count += a * self.d[point[0] + edge][point[1] - edge] * self.d[point[0] + edge][point[1]]
            elif x > point[1]:
                edge = x - point[1]
                a = self.d[point[0]][x]
                if point[0] + edge in self.d.keys() and point[1] + edge in self.d[point[0] + edge].keys() and point[1] in self.d[point[0] + edge].keys():
                    count += a * self.d[point[0] + edge][point[1] + edge] * self.d[point[0] + edge][point[1]]
                if point[0] - edge in self.d.keys() and point[1] + edge in self.d[point[0] - edge].keys() and point[1] in self.d[point[0] - edge].keys():
                    count += a * self.d[point[0] - edge][point[1] + edge] * self.d[point[0] - edge][point[1]]
        return count


demo = DetectSquares()
demo.add([3,10])
demo.add([11,2])
demo.add([3,2])
print(demo.count([11,10]))
print(demo.count([14,8]))
demo.add([11,2])
print(demo.count([11,10]))


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)