"""
============
3D animation
============

A simple example of an animated plot... In 3D!
"""
import numpy as np

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.animation as animation

X = np.arange(0, 10)
Y = np.arange(0, 10)
Z = np.arange(0, 10)

"""
============
3D animation
============

A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


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


planes = {}


def Gen_RandLine(length, dims=2):
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)  # 初始化起点
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)  # 步长
        # 下一步的位置
        lineData[:, index] = lineData[:, index - 1] + step

    return lineData  # 返回一个shape为（3,25）的数组,3维坐标25帧


def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines


def update_plane(ax):
    for index in range(1, planes.__len__() + 1):
        if index <= 10:
            planes[index].z - 1
            p = planes[index]
            ax.scatter(p.x, p.y, p.z)


z = np.arange(9, 7, -0.1)
fig = plt.figure()
ax = p3.Axes3D(fig)


def draw_plane(plane):
    # ax.scatter(plane.x, plane.y, plane.z)
    # ax.scatter(plane.x, plane.y, plane.z)
    line, = ax.plot([plane.x], [plane.y], [plane.z], marker='o', color='red', markersize=8)


# dot = ax.scatter(5, 4, z)
y, z = 4, 10


def init_datas():
    for index in range(1, 21):
        if index <= 10:
            y = 3
            p = Plane(index, y, z)
            planes[index] = p
            draw_plane(p)
        else:
            y = 6
            x = index - 10
            p = Plane(x, y, z)
            planes[index] = p
            draw_plane(p)

    return planes


def update_dot(i):
    dot.z = 10 - i
    return dot,


def init_dot():
    return dot,


if __name__ == '__main__':
    # Attaching 3D axis to the figure
    # fig = plt.figure()
    # ax = p3.Axes3D(fig)

    # Fifty lines of random 3-D lines  (长为50的数组，每个元素为shape为3,25的ndarray，最后实际效果就是50条路径)
    # data = [Gen_RandLine(25, 3) for index in range(50)]
    #
    # # Creating fifty line objects.
    # # NOTE: Can't pass empty arrays into 3d version of plot()
    # lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]  # 每条路径的起始点

    # Setting the axes properties
    ax.set_xlim3d([0.0, 12.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, 12.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 12.0])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')

    # Creating the Animation object
    # line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
    #                                    interval=50, blit=False)
    #
    # y, z = 4, 10

    init_datas()
    # animation.FuncAnimation(fig, func=update_dot, frames=5, interval=500)

    plt.show()
