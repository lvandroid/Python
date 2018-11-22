import matplotlib
import numpy as np
import matplotlib as mpl

mpl.use("TkAgg")
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animmation
import copy
import matplotlib.font_manager as fm

# 解决中文乱码问题
myfont = fm.FontProperties(fname="/Library/Fonts/Songti.ttc", size=14)
matplotlib.rcParams["axes.unicode_minus"] = False

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
    def to_up(self):
        self.z += 1
        return self

        # 上升

    def to_up(self, z):
        self.z += z
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

lines = []


def set_data_line(p, plane):
    p.set_data([plane.x, plane.y])
    p.set_3d_properties(plane.z)
    return p


def fly_up(z, planes):
    for p in planes.values():
        p.to_up(z)


def fly_down(z, planes):
    for p in planes.values():
        p.to_down(z)


def fly_left(x, planes):
    for p in planes.values():
        p.to_left(x)


def fly_right(x, planes):
    for p in planes.values():
        p.to_right(x)


def fly_forward(y, planes):
    for p in planes.values():
        p.to_forward(y)


def fly_back(y, planes):
    for p in planes.values():
        p.to_back(y)


# 旋转90°,每个元素先向上移动index步，再右移index步
def right_angle_90(planes):
    for key, p in planes.items():
        p.to_up(key)
        p.to_right(key)


def left_angle_90(planes):
    for key, p in planes.items():
        p.to_up(key)
        p.to_left(key)


def front_angle_90(planes):
    for key, p in planes.items():
        p.to_forward(key * _distance_)
        p.to_left(-key * _distance_)


# def draw_red_line(plane, c):
def draw_line(plane, c):
    return ax.plot([plane.x], [plane.y], [plane.z], marker='o', color=c, markersize=8)


def draw_lines(c, planes=[]):
    for index in range(0, planes.length):
        draw_line(planes[index], c)


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
    fly_up(3, arr_big_first)
    right_angle_90(arr_small_first)
    left_angle_90(arr_small_second)
    right_angle_90(arr_small_third)
    left_angle_90(arr_small_fourth)

    fly_up(4, arr_small_first)
    fly_forward(_distance_, arr_small_first)
    fly_left(2, arr_small_first)

    fly_up(4, arr_small_second)
    fly_forward(_distance_, arr_small_second)
    fly_right(2, arr_small_second)

    fly_up(4, arr_small_third)

    fly_up(4, arr_small_fourth)
    fly_back(_distance_, arr_small_second)


# 飞成9数字图形
def fly_9():
    fly_up(6, arr_big_second)
    fly_up(9, arr_big_third)
    fly_right(8, arr_big_second)
    fly_left(8, arr_big_third)

    fly_up(3, arr_small_first)
    fly_up(3, arr_small_third)

    fly_up(3, arr_small_second)

    fly_right(3, arr_small_first)
    fly_right(3, arr_small_third)

    fly_left(3, arr_small_second)
    fly_left(3, arr_small_fourth)


def fly_8():
    fly_9()
    fly_down(3, arr_small_first)
    fly_back(_distance_, arr_small_first)


def fly_7():
    fly_8()
    front_angle_90(arr_big_first)


def fly_6():
    fly_8()
    fly_forward(_distance_, arr_small_second)
    fly_down(3, arr_small_second)


def fly_5():
    fly_6()
    fly_forward(_distance_, arr_small_first)
    fly_up(3, arr_small_first)


def fly_4():
    pass


def fly_3():
    fly_5()
    fly_right(3, arr_small_first)
    fly_right(3, arr_small_third)


def fly_2():
    fly_3()
    fly_left(3, arr_small_second)
    fly_left(3, arr_small_fourth)


def fly_1():
    pass


def fly_0():
    pass


def init():
    init_planes()
    start_fly()
    # fly_9()
    # fly_8()
    # fly_7()
    # fly_6()
    # fly_5()
    # fly_3()
    fly_2()
    for index in range(0, 4):
        if index < 2:
            ls_21, = draw_line(arr_small_first[index], 'blue')
            lines.append(ls_21)
            ls_22, = draw_line(arr_small_second[index], 'blue')
            lines.append(ls_22)
            ls_23, = draw_line(arr_small_third[index], 'purple')
            lines.append(ls_23)
            ls_24, = draw_line(arr_small_fourth[index], 'purple')
            lines.append(ls_24)
        ls_41, = draw_line(arr_big_first[index], 'red')
        lines.append(ls_41)
        ls_42, = draw_line(arr_big_second[index], 'blue')
        lines.append(ls_42)
        ls_43, = draw_line(arr_big_third[index], 'green')
        lines.append(ls_43)

    return lines


def update(data):
    i = 0
    if i < 4:
        for index in range(0, 4):
            lines[i] = set_data_line(lines[i], data[0][index])
            i += 1

    if 4 <= i < 8:
        for index in range(0, 4):
            lines[i] = set_data_line(lines[i], data[1][index])
            i += 1
    if 8 <= i < 12:
        for index in range(0, 4):
            lines[i] = set_data_line(lines[i], data[2][index])
            i += 1
    if 12 <= i < 14:
        for index in range(0, 2):
            lines[i] = set_data_line(lines[i], data[3][index])
            i += 1
    if 14 <= i < 16:
        for index in range(0, 2):
            lines[i] = set_data_line(lines[i], data[4][index])
            i += 1
    if 16 <= i < 18:
        for index in range(0, 2):
            lines[i] = set_data_line(lines[i], data[5][index])
            i += 1
    if 18 <= i < 20:
        for index in range(0, 2):
            lines[i] = set_data_line(lines[i], data[6][index])
            i += 1

    return lines


def data_gen():
    global x0, y0, z0
    data = []
    for ti in range(1, 10):
        fly_up(5, arr_small_fourth)
        data.append(
            [arr_big_first,
             arr_big_second,
             arr_big_third,
             arr_small_first,
             arr_small_second,
             arr_small_third,
             arr_small_fourth]
        )
    return data


if __name__ == '__main__':
    ax.set_aspect('equal')
    ax.set_title("无人机飞行模型--数字2", fontproperties=myfont)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-6, 6])
    ax.set_zlim([0, 10])

    # ani = animmation.FuncAnimation(f, update, frames=data_gen(), init_func=init, interval=_interval_)
    init()
    # init_planes()
    # update(init())

    plt.show()
