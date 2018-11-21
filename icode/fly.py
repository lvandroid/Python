import numpy as np
import matplotlib as mpl

mpl.use("TkAgg")
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animmation
import copy


class Plane:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # def __x__(self):
    #     return self.x
    #
    # def __y__(self):
    #     return self.y
    #
    # def __z__(self):
    #     return self.z

    # 左翻
    def turn_left(self):
        self.x -= 1
        return self

    # 右翻
    def turn_right(self):
        self.x += 1
        return self

    # 前翻
    def turn_forward(self):
        self.y += 1
        return self

    # 后翻
    def turn_back(self):
        self.y -= 1
        return self

    # 左飞
    def to_left(self):
        self.x -= 1
        return self

        # 左飞

    def to_left(self, x):
        self.x -= x
        return self

    # 右飞
    def to_right(self):
        self.x += 1
        return self
        # 右飞

    def to_right(self, x):
        self.x += x
        return self

    # 前飞
    def to_forward(self):
        self.y += 1
        return self

    def to_forward(self, y):
        self.y += y
        return self

    # 后飞
    def to_back(self):
        self.y -= 1
        return self

        # 后飞

    def to_back(self, y):
        self.y -= y
        return self

    # 上升
    def to_upper(self):
        self.z += 1
        return self

    # 下降
    def to_down(self):
        self.z -= 1
        return self

    def to_down(self, z):
        self.z -= z
        return self


# 飞机间距
_distance_ = 1
# 飞机动画更新时间间隔，越大，变化越慢
_interval_ = 200

f = plt.figure(figsize=(6, 6))
ax = f.add_subplot(111, projection='3d')

# 初始化飞机位置
x0 = 0
y0 = 0
z0 = 0

# 初始化的飞机
plane_first = Plane(x0, y0, z0)
# 四个飞机一组 有3组

# 第一组，x 从1-4
arr_big_first = {}
arr_big_second = {}
arr_big_third = {}

# 两架飞机一组，有4组
arr_small_first = {}
arr_small_second = {}
arr_small_third = {}
arr_small_fourth = {}


# 初始化飞机数据
def init_planes():
    for index in range(0, 4):
        arr_big_first[index] = copy.copy(plane_first).to_right((index) * _distance_)
        arr_big_second[index] = copy.copy(plane_first).to_left((index + 5) * _distance_)
        arr_big_third[index] = copy.copy(plane_first).to_right((index + 8) * _distance_)
    for index in range(0, 2):
        arr_small_first[index] = copy.copy(plane_first).to_left((index + 1) * _distance_)
        arr_small_second[index] = copy.copy(plane_first).to_right((4 + index) * _distance_)
        arr_small_third[index] = copy.copy(plane_first).to_left((3 + index) * _distance_)
        arr_small_fourth[index] = copy.copy(plane_first).to_right((6 + index) * _distance_)


# 20架飞机 开始是一字排开，起飞后调整位置(即初始化这7个列表)，以后的倒计时图案只需要执行整个列表就可以变化图形
def start_fly():
    pass


def set_data(p, plane):
    p.set_data([plane.x, plane.y])
    p.set_3d_properties(plane.z)
    return p


# def draw_red_line(plane, c):
def draw_line(plane, c):
    return ax.plot([plane.x], [plane.y], [plane.z], marker='o', color=c, markersize=8)


def update(data):
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20
    plane1 = data[0]
    p1.set_data([plane1.x, plane1.y])
    p1.set_3d_properties(plane1.z)
    plane2 = data[1]
    p2.set_data([plane2.x, plane2.y])
    p2.set_3d_properties(plane2.z)
    p3 = set_data(p3, data[2])
    p4 = set_data(p4, data[3])
    p5 = set_data(p5, data[4])
    p6 = set_data(p6, data[5])
    p7 = set_data(p7, data[6])
    p8 = set_data(p8, data[7])

    return p1, p2, p3, p4, p5, p6, p7, p8


def init():
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20
    init_planes()
    p1, = draw_line(arr_big_first[0], 'red')
    p2, = draw_line(arr_big_first[1], 'red')
    p3, = draw_line(arr_big_first[2], 'red')
    p4, = draw_line(arr_big_first[3], 'red')

    p5, = draw_line(arr_big_second[0], 'blue')
    p6, = draw_line(arr_big_second[1], 'blue')
    p7, = draw_line(arr_big_second[2], 'blue')
    p8, = draw_line(arr_big_second[3], 'blue')

    p9, = draw_line(arr_big_third[0], 'green')
    p10, = draw_line(arr_big_third[1], 'green')
    p11, = draw_line(arr_big_third[2], 'green')
    p12, = draw_line(arr_big_third[3], 'green')

    p13, = draw_line(arr_small_first[0], 'green')
    p14, = draw_line(arr_small_first[1], 'green')

    p15, = draw_line(arr_small_second[0], 'blue')
    p16, = draw_line(arr_small_second[1], 'blue')

    p17, = draw_line(arr_small_third[0], 'purple')
    p18, = draw_line(arr_small_third[1], 'purple')

    p19, = draw_line(arr_small_fourth[0], 'purple')
    p20, = draw_line(arr_small_fourth[1], 'purple')

    # p00 = Plane(x0, y0, z0)
    # p11 = copy.copy(p00)
    # p12 = copy.copy(p11).to_right()
    # p13 = copy.copy(p12).to_right()
    # p14 = copy.copy(p13).to_right()

    # p21 = copy.copy(p00).to_forward(4 * _distance_)
    # p22 = copy.copy(p21).to_right()
    # p23 = copy.copy(p22).to_right()
    # p24 = copy.copy(p23).to_right()
    #
    # p31 = copy.copy(p00).to_down(10 * _distance_).to_forward(2 * _distance_)
    # p32 = copy.copy(p31).to_right()
    # p33 = copy.copy(p32).to_right()
    # p34 = copy.copy(p33).to_right()
    #
    # p41 = copy.copy(p21).to_down(5 * _distance_).to_back(3 * _distance_)
    # p42 = copy.copy(p41).to_right()
    #
    # p51 = copy.copy(p41).to_forward(3 * _distance_)
    # p52 = copy.copy(p51).to_right()
    #
    # p1, = draw_line(p11, 'red')
    # p2, = draw_line(p12, 'red')
    # p3, = draw_line(p13, 'red')
    # p4, = draw_line(p14, 'red')
    #
    # p5, = draw_line(p21, 'green')
    # p6, = draw_line(p22, 'green')
    # p7, = draw_line(p23, 'green')
    # p8, = draw_line(p24, 'green')
    #
    # p9, = draw_line(p31, 'blue')
    # p10, = draw_line(p32, 'blue')
    # p11, = draw_line(p33, 'blue')
    # p12, = draw_line(p34, 'blue')
    #
    # p13, = draw_line(p41, 'purple')
    # p14, = draw_line(p42, 'purple')
    #
    # p15, = draw_line(p51, 'green')
    # p16, = draw_line(p52, 'green')

    # return p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20
    return p1, p2, p3, p4


def data_gen():
    global x0, y0, z0
    data = []
    for ti in range(1, 10):
        xt1 = x0
        yt1 = y0
        zt1 = z0 - ti
        p1 = Plane(xt1, yt1, zt1)
        p2 = copy.copy(p1).to_right()
        p3 = copy.copy(p2).to_right()
        p4 = copy.copy(p3).to_right()

        p21 = Plane(x0, y0 + 3, z0 + ti)
        p22 = copy.copy(p21).to_right()
        p23 = copy.copy(p22).to_right()
        p24 = copy.copy(p23).to_right()
        data.append([p1, p2, p3, p4, p21, p22, p23, p24])
    return data


if __name__ == '__main__':
    ax.set_aspect('equal')
    ax.set_title("Dot Move")
    ax.set_xlim([-8, 8])
    ax.set_ylim([-6, 6])
    ax.set_zlim([-10, 10])

    # ani = animmation.FuncAnimation(f, update, frames=data_gen(), init_func=init, interval=_interval_)
    init()
    # init_planes()

    plt.show()
