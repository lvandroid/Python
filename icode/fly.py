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

    # 右飞
    def to_right(self):
        self.x += 1
        return self

    # 前飞
    def to_forward(self):
        self.y += 1
        return self

    # 后飞
    def to_back(self):
        self.y -= 1
        return self

    # 上升
    def to_upper(self):
        self.z += 1
        return self

    # 下降
    def to_down(self):
        self.z -= 1
        return self


# 飞机间距
_distance_ = 1
# 飞机动画更新时间间隔，越大，变化越慢
_interval_ = 100

f = plt.figure(figsize=(6, 6))
ax = f.add_subplot(111, projection='3d')

# 初始化飞机位置
x0 = 3
y0 = 3
z0 = 15


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

    return p1, p2, p3


def init():
    global p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20
    plane0 = Plane(x0, y0, z0)
    plane2 = copy.copy(plane0).to_left()
    plane3 = copy.copy(plane0).to_right()
    p1, = draw_line(plane0, 'red')
    p2, = draw_line(plane2, 'green')
    p3, = draw_line(plane3, 'blue')

    return p1, p2, p3


def data_gen():
    global x0, y0, z0
    data = []
    for ti in range(1, 20):
        xt1 = x0
        yt1 = y0
        zt1 = z0 - ti / 2
        p1 = Plane(xt1, yt1, zt1)
        p2 = copy.copy(p1).to_left()
        p3 = copy.copy(p1).to_right()
        data.append([p1, p2, p3])
    return data


if __name__ == '__main__':
    ax.set_aspect('equal')
    ax.set_title("Dot Move")
    ax.set_xlim([0, 15])
    ax.set_ylim([0, 15])
    ax.set_zlim([0, 15])

    ani = animmation.FuncAnimation(f, update, frames=data_gen(), init_func=init, interval=_interval_)

    plt.show()
