import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.font_manager as fm

# 解决中文乱码问题
myfont = fm.FontProperties(fname="/Library/Fonts/Songti.ttc", size=14)
matplotlib.rcParams["axes.unicode_minus"] = False

planes = {}


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


p0 = Plane(5, 5, 10)


def init():
    global line1
    p1 = Plane(5, 5, 10)

    xt1 = x0,
    yt1 = y0,
    zt1 = z0 - 1

    # line1, = ax.plot([xt1], [yt1], [zt1], marker='o', color='blue')
    line1, = ax.plot([xt1], [yt1], [zt1], marker='o', color='blue', markersize=8)
    return line1


def update(data):
    global line1
    line1.set_data([data[0], data[1]])
    line1.set_3d_properties(data[2])
    return line1


def data_gen():
    global x0, y0, z0
    data = []
    for i in range(1, 5):
        xt1 = x0
        yt1 = y0
        zt1 = z0 - i
        data.append([xt1, yt1, zt1])
    return data


x0, y0, z0 = 5, 5, 10
x1, y1, z1 = x0, y0, z0

f = plt.figure(figsize=(6, 6))
ax = f.add_subplot(111, projection='3d')
# init()
ax.set_xlim3d([0.0, 12.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 12.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 12.0])
ax.set_zlabel('Z')
ax.plot([x1], [y1], [z1], 'r')
animation.FuncAnimation(f, update, frames=data_gen(), init_func=init, interval=1000)
ax.set_title('三维散点动画', fontproperties=myfont)
plt.show()
