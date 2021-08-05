# 给定一个包含非负整数的数组，
# 你的任务是统计其中可以组成三角形三条边的三元组个数。
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
# perm：A,comb:C
from typing import List
from scipy.special import comb, perm


class Node:
    def __init__(self, value):
        self.value = value
        self.value_count = 0
        self.prev = None
        self.next = None

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 设计一个数组最大长度的字典
        # 不设置字典了，但数量为0时为不存在
        # data = dict.fromkeys(range(0,max(nums)), False)
        # 会有重复元素，所以在设置一个每个元素的计数器吧，并初始化
        num_count = [0] * (max(nums) + 1)
        for i in nums:
            num_count[i] += 1
        triangle_count = 0
        max_num = max(nums)
        temp = []
        # 选取任意两个数，则从两数之差的绝对值到两数之和，有的话，则可以组成三角形
        # for index in range(0, len(nums)-2):
        #     # 将第一个数删除，并设置一个暂存序列.
        #     num_count[nums[index]] -= 1
        #     temp = num_count.copy()
        #     for inner_index in range(index + 1, len(nums)-1):
        #         temp[nums[inner_index]] -= 1
        #         print('最内循环的前两个边是：{0}，{1}'.format(nums[index], nums[inner_index]))
        #         # print('循环范围是：{0}，{1}'.format(abs(nums[index] - nums[inner_index]) + 1,nums[inner_index] + nums[index] - 1))
        #         for inner_inner_index in \
        #                 range(abs(nums[index] - nums[inner_index]) + 1,
        #                       nums[inner_index] + nums[index]):
        #             # print('前两条边条边是：{0}，{1}，准备查看的数是{2}'.format(nums[index], nums[inner_index], inner_inner_index))
        #             # print('num_count的值是：', num_count)
        #             if inner_inner_index <= max_num:
        #                 if temp[inner_inner_index] > 0:
        #                     # print('进入测试的三条边是：{0}，{1}，{2}'.format(nums[index], nums[inner_index], inner_inner_index))
        #                     if self.is_triangle(nums[index], nums[inner_index], inner_inner_index):
        #                         triangle_count += num_count[inner_inner_index]
        #                         # print('测试成功的三条边是：{0}，{1}，{2}'.format(nums[index], nums[inner_index], inner_inner_index))
        #         print('当前的数值是：',triangle_count)

        for index in range(1, len(num_count)):
            if num_count[index] > 0:
                a = num_count[index]
                num_count[index] -= 1
                temp = num_count.copy()
                for inner_index in range(index, len(temp)):
                    if temp[inner_index] > 0:
                        b = temp[inner_index]
                        temp[inner_index] -= 1
                        # inner_temp = temp.copy()
                        for inner_inner_index in \
                                range(abs(index - inner_index) + 1, inner_index + index):
                            if inner_inner_index <= max_num:
                                if temp[inner_inner_index] > 0:
                                    temp_a = a
                                    temp_b = b
                                    if self.is_triangle(index, inner_index, inner_inner_index):
                                        # print('测试成功的三条边是：{0}，{1}，{2}'.format(index, inner_index, inner_inner_index))
                                        # print('temp_a:{0},temp_b:{1},temp[{2}]:{3}'.format(temp_a, temp_b,
                                        #                                                    inner_inner_index,
                                        #                                                    temp[inner_inner_index]))
                                        # print('这三条边的组合有{0}种'.format(temp_a * temp_b * temp[inner_inner_index]))
                                        # 三边相等
                                        if inner_inner_index == index == inner_index:
                                            triangle_count += comb(a, 3)
                                        # 两边相等
                                        elif inner_inner_index == inner_index:
                                            triangle_count += comb(b, 2) * a
                                        elif inner_index == index:
                                            triangle_count += comb(a, 2) * temp[inner_inner_index]
                                        elif index == inner_inner_index:
                                            triangle_count += comb(a, 2) * b
                                        else:
                                            triangle_count += a * b * temp[inner_inner_index]

                                        # triangle_count += temp_a * temp_b * temp[inner_inner_index]
                                        # temp[inner_inner_index] = 0

                        temp[inner_index] = 0
                num_count[index] = 0
        return int(triangle_count)

    @staticmethod
    def is_triangle(index, inner_index, inner_inner_index):
        if (index + inner_index) > inner_inner_index \
                and (inner_index + inner_inner_index) > index \
                and (index + inner_inner_index) > inner_index:
            return True
        else:
            return False

    def method_2(self, nums: List[int]) -> int:
        triangle_count = 0
        for index in range(0, len(nums) - 2):
            for inner_index in range(index + 1, len(nums) - 1):
                # print('最内循环的前两个边是：{0}，{1}'.format(nums[index], nums[inner_index]))
                for inner_inner_index in range(inner_index + 1, len(nums)):
                    if self.is_triangle(nums[index], nums[inner_index], nums[inner_inner_index]):
                        print('测试成功的三条边是：{0}，{1}，{2}'.format(nums[index], nums[inner_index], nums[inner_inner_index]))
                        triangle_count += 1
                # print('当前的数值是：', triangle_count)
        return triangle_count


demo = Solution()
# 时间超出了限制，能怎么办呢，暂时想出的是之前的那种列表保存余额的用法
# 有没有一种数据结构 可以将数据从小到大保存，并且记录到
#
# print(demo.triangleNumber(nums=[2, 2, 3, 4]))
# print(demo.triangleNumber(nums=[34, 75, 96, 10, 60, 70, 70, 45]))
# print(demo.triangleNumber(nums=[0, 1, 1, 1]))
# print(demo.triangleNumber(nums=[2, 2, 2, 3]))
print(demo.triangleNumber(nums=
                          [874, 979, 60, 893, 62, 872, 59, 936, 1, 912, 623, 985, 807, 62, 546, 733, 363, 424, 36, 152,
                           987, 748, 787, 785, 7, 733, 802, 279, 688, 947, 59, 413, 451, 234, 943, 692, 926, 496, 532,
                           537, 455, 919, 491, 133, 814, 642, 344, 641, 377, 960, 122, 731, 566, 564, 956, 803, 299,
                           740, 843, 57, 531, 225, 294, 878, 57, 105, 416, 172, 384, 96, 817, 82, 846, 130, 751, 855,
                           151, 579, 562, 117, 738, 784, 25, 620, 968, 231, 637, 670, 40, 280, 1, 31, 613, 545, 273,
                           325, 283, 5, 218, 192, 897, 556, 539, 627, 253, 430, 493, 673, 808, 220, 900, 798, 467, 141,
                           319, 87, 916, 559, 159, 191, 89, 398, 697, 396, 235, 700, 84, 732, 964, 481, 361, 858, 672,
                           518, 849, 872, 320, 949, 285, 727, 583, 337, 299, 654, 357, 707, 900, 737, 624, 138, 620,
                           407, 93, 924, 744, 875, 843, 916, 447, 244, 337, 409, 252, 60, 982, 337, 362, 610, 162, 339,
                           75, 290, 720, 978, 910, 148, 164, 908, 727, 711, 449, 402, 79, 708, 331, 569, 753, 471, 829,
                           199, 782, 111, 553, 486, 120, 678, 341, 718, 655, 945, 344, 397, 823, 37, 882, 870, 707, 714,
                           137, 270, 230, 595, 570, 290, 911, 614, 239, 490, 129, 734, 976, 395, 150, 238, 347, 569, 11,
                           613, 292, 126, 169, 772, 333, 543, 247, 854, 438, 45, 717, 506, 422, 961, 295, 711, 320, 551,
                           682, 106, 716, 82, 4, 785, 493, 544, 354, 399, 34, 10, 822, 291, 6, 886, 222, 801, 210, 892,
                           131, 40, 883, 49, 389, 142, 390, 983, 24, 169, 841, 211, 263, 136, 428, 427, 958, 167, 687,
                           606, 578, 743, 153, 168, 10, 969, 546, 489, 833, 809, 769, 882, 180, 347, 24, 766, 673, 622,
                           202, 52, 582, 410, 197, 14, 149, 199, 268, 252, 619, 639, 418, 810, 226, 918, 326, 299, 382,
                           724, 74, 192, 993, 951, 113, 881, 535, 775, 593, 856, 172, 862, 551, 419, 763, 70, 576, 15,
                           928, 237, 436, 399, 88, 802, 504, 105, 182, 92, 646, 41, 696, 343, 360, 760, 593, 702, 500,
                           392, 504, 442, 341, 715, 185, 531, 446, 29, 980, 127, 439, 244, 126, 330, 790, 223, 526, 22,
                           56, 958, 510, 368, 601, 701, 919, 219, 140, 573, 232, 696, 359, 99, 97, 473, 974, 567, 810,
                           76, 899, 57, 278, 694, 650, 899, 663, 875, 561, 646, 897, 201, 621, 515, 177, 257, 408, 613,
                           584, 981, 199, 126, 978, 263, 892, 576, 482, 800, 238, 946, 96, 956, 921, 740, 541, 552, 295,
                           721, 4, 986, 854, 719, 467, 650, 326, 976, 572, 580, 493, 86, 757, 741, 547, 520, 540, 573,
                           972, 312, 219, 707, 46, 605, 862, 248, 405, 283, 544, 770, 285, 478, 501, 590, 913, 331, 92,
                           937, 321, 679, 518, 567, 112, 530, 975, 965, 537, 421, 347, 6, 77, 958, 379, 330, 739, 427,
                           306, 788, 74, 119, 624, 150, 832, 977, 148, 654, 266, 135, 142, 735, 579, 703, 528, 467, 880,
                           698, 609, 340, 799, 99, 696, 77, 855, 388, 243, 995, 510, 194, 695, 973, 240, 512, 846, 163,
                           874, 531, 80, 117, 714, 227, 618, 717, 243, 638, 496, 725, 917, 748, 990, 440, 172, 723, 260,
                           507, 606, 863, 602, 138, 93, 115, 756, 97, 238, 94, 343, 602, 788, 199, 305, 657, 243, 560,
                           199, 274, 343, 310, 849, 148, 236, 848, 382, 995, 421, 822, 607, 306, 42, 722, 73, 787, 488,
                           7, 484, 822, 281, 400, 389, 64, 750, 59, 678, 86, 625, 398, 45, 341, 437, 640, 400, 282, 844,
                           746, 589, 450, 147, 87, 888, 742, 447, 584, 989, 530, 68, 530, 181, 6, 666, 548, 630, 816,
                           108, 499, 433, 379, 301, 294, 963, 301, 884, 551, 468, 436, 387, 518, 929, 873, 819, 2, 442,
                           228, 55, 523, 663, 116, 204, 7, 838, 287, 286, 81, 612, 823, 866, 243, 397, 548, 932, 711,
                           776, 775, 587, 594, 204, 41, 506, 809, 184, 776, 42, 634, 382, 260, 124, 982, 970, 164, 394,
                           930, 397, 37, 926, 789, 296, 365, 420, 274, 735, 760, 411, 517, 137, 23, 167, 471, 779, 288,
                           582, 500, 670, 47, 142, 560, 180, 508, 890, 193, 952, 314, 669, 554, 554, 616, 330, 874, 150,
                           684, 661, 426, 964, 103, 35, 247, 259, 132, 188, 972, 499, 553, 138, 771, 972, 723, 801, 108,
                           589, 264, 688, 222, 682, 374, 21, 328, 500, 311, 987, 112, 991, 543, 855, 801, 387, 69, 795,
                           536, 562, 564, 305, 10, 500, 411, 109, 434, 770, 876, 655, 764, 287, 964, 863, 237, 302, 88,
                           91, 696, 900, 231, 451, 595, 58, 257, 731, 849, 668, 143, 352, 581, 277, 418, 531, 537, 119,
                           292, 98, 279, 65, 105, 217, 921, 754, 897, 142, 825, 205, 499, 890, 375, 980, 868, 233, 492,
                           124, 70, 157, 570, 1000, 205, 321, 405, 302, 56, 807, 910, 610, 799, 290, 227, 334, 901, 23,
                           980, 784, 599, 805, 96, 143, 183, 635, 916, 404, 630, 337, 850, 358, 136, 571, 774, 524, 350,
                           60, 871, 156, 120, 750, 439, 624, 616, 926, 148, 471, 161, 181, 318, 692, 730, 343, 495, 536,
                           732, 444, 374, 258, 425, 754, 270, 817, 871, 344, 523, 263, 22, 266, 883, 779, 145, 951, 860,
                           782, 989, 39, 873, 148, 854, 14, 1, 932, 774, 263, 739, 46, 821, 546, 871, 687, 151, 574,
                           920, 479, 322, 954, 822, 326, 747, 897, 265, 181, 559, 681, 297, 258, 579, 498, 774, 864,
                           931, 431, 828, 724, 978, 172, 829, 964, 612, 285, 909, 874, 514, 102, 884, 325, 408, 248,
                           493, 550]))
# 正确答案是36
