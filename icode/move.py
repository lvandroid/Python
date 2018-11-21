import numpy as np
import matplotlib as mpl

mpl.use("TkAgg")
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animmation

# 飞机间距
_distance_ = 1
# 飞机动画更新时间间隔，越大，变化越慢
_interval_ = 200


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


f = plt.figure(figsize=(6, 6))
ax = f.add_subplot(111, projection='3d')

x0 = 3
y0 = 3
z0 = 15


def update(data):
    global p1, p2, p3, p4, p5, p6, p7, p8
    p1.set_data([data[0], data[1]])
    p1.set_3d_properties(data[2])
    p2.set_data([data[3], data[4]])
    p2.set_3d_properties(data[5])
    p3.set_data([data[6], data[7]])
    p3.set_3d_properties(data[8])
    p4.set_data([data[9], data[10]])
    p4.set_3d_properties(data[11])
    p5.set_data([data[12], data[13]])
    p5.set_3d_properties(data[14])
    p6.set_data([data[15], data[16]])
    p6.set_3d_properties(data[17])
    p7.set_data([data[18], data[19]])
    p7.set_3d_properties(data[20])
    p8.set_data([data[21], data[22]])
    p8.set_3d_properties(data[23])

    return p1, p2, p3, p4, p5, p6, p7, p8
    # return p1


def init():
    global p1, p2, p3, p4, p5, p6, p7, p8
    xt1 = x0
    yt1 = y0
    zt1 = z0

    p1, = ax.plot([xt1], [yt1], [zt1], marker='o', color='red', markersize=8)
    p2, = ax.plot([xt1 + 1], [yt1], [zt1], marker='o', color='red', markersize=8)
    p3, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='red', markersize=8)
    p4, = ax.plot([xt1 + 3], [yt1], [zt1], marker='o', color='red', markersize=8)

    p5, = ax.plot([xt1], [yt1+3], [zt1 + 2], marker='o', color='blue', markersize=8)
    p6, = ax.plot([xt1 + 1], [yt1+3], [zt1 + 2], marker='o', color='blue', markersize=8)
    p7, = ax.plot([xt1 + 2], [yt1+3], [zt1 + 2], marker='o', color='blue', markersize=8)
    p8, = ax.plot([xt1 + 3], [yt1+3], [zt1 + 2], marker='o', color='blue', markersize=8)

    p9, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)
    p10, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)

    p11, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)
    p12, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)
    p13, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)
    p14, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)

    p15, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)
    p16, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)
    p17, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)
    p18, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)

    p19, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)
    p20, = ax.plot([xt1 + 2], [yt1], [zt1], marker='o', color='blue', markersize=8)

    return p1, p2, p3, p4, p5, p6, p7, p8
    # return p1


def data_gen():
    global x0, y0, z0
    data = []
    for ti in range(1, 100):
        xt1 = x0
        yt1 = y0
        zt1 = z0 - ti / 10
        data.append([xt1, yt1, zt1])
    return data


def data_gen2():
    global x0, y0, z0
    data = []
    for ti in range(1, 10):
        xt1 = x0
        yt1 = y0
        zt1 = z0 - ti
        data.append([xt1, yt1, zt1,
                     xt1 + _distance_, yt1, zt1,
                     xt1 + 2 * _distance_, yt1, zt1,
                     xt1 + 3 * _distance_, yt1, zt1,
                     xt1 + _distance_, yt1+2*_distance_, zt1 + 2,
                     xt1 + 2 * _distance_, yt1+2*_distance_, zt1 + 2,
                     xt1 + 3 * _distance_, yt1+2*_distance_, zt1 + 2,
                     xt1 + 4 * _distance_, yt1+2*_distance_, zt1 + 2])
    return data


t_drange = np.arange(0, 1, 0.01)
t_dlen = len(t_drange)

ax.set_aspect('equal')
ax.set_title("Dot Move")
ax.set_xlim([0, 15])
ax.set_ylim([0, 15])
ax.set_zlim([0, 15])
# ani = animmation.FuncAnimation(f, update, frames=data_gen(), init_func=init, interval=20)
# plt.pause(1000)
ani = animmation.FuncAnimation(f, update, frames=data_gen2(), init_func=init, interval=_interval_)
plt.show()
