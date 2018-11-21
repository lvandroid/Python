import numpy as np
import matplotlib as mpl

mpl.use("TkAgg")
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animmation

r1 = 10
r2 = 1
omega1 = 2 * np.pi
omega2 = 24 * np.pi
phi = 5.1454 * np.pi / 180


def update(data):
    global line1, line2, line3, line4, line5, line6, line7, line8, line9

    line1.set_data([data[0], data[1]])
    line1.set_3d_properties(data[2])
    line2.set_data([data[3], data[4]])
    line2.set_3d_properties(data[5])
    line3.set_data([data[6], data[7]])
    line3.set_3d_properties(data[8])
    line4.set_data([data[9], data[10]])
    line4.set_3d_properties(data[11])
    line5.set_data([data[12], data[13]])
    line5.set_3d_properties(data[14])
    line6.set_data([data[15], data[16]])
    line6.set_3d_properties(data[17])
    line7.set_data([data[18], data[19]])
    line7.set_3d_properties(data[20])
    line8.set_data([data[21], data[22]])
    line8.set_3d_properties(data[23])
    line9.set_data([data[24], data[25]])
    line9.set_3d_properties(data[26])
    # return line1, line2, line3,
    # return line1
    # return line1, line2
    return line1, line2, line3, line4, line5, line6, line7, line8, line9
    # return  line2, line3,


def init():
    global line1, line2, line3, line4, line5, line6, line7, line8, line9
    ti = 0
    # t = t_drange[np.mod(ti, t_dlen)]

    xt1 = x0
    yt1 = y0
    zt1 = z0
    xt2 = x_2
    yt2 = y_2
    zt2 = z_2
    xt3 = x_3
    yt3 = y_3
    zt3 = z_3
    xt4 = x_4
    yt4 = y_4
    zt4 = z_4
    xt5 = x_5
    yt5 = y_5
    zt5 = z_5
    xt6 = x_6
    yt6 = y_6
    zt6 = z_6
    xt7 = x_7
    yt7 = y_7
    zt7 = z_7
    xt8 = x_8
    yt8 = y_8
    zt8 = z_8
    xt9 = x_9
    yt9 = y_9
    zt9 = z_9
    # xt21 = xt1 + r2 * np.sin(2 * np.pi * t_range)
    # yt21 = yt1 + r2 * np.cos(2 * np.pi * t_range) / (np.cos(phi) * (1 + np.tan(phi) ** 2))
    # zt21 = zt1 + (yt21 - yt1) * np.tan(phi)

    line1, = ax.plot([xt1], [yt1], [zt1], marker='o', color='blue', markersize=8)
    line2, = ax.plot([xt2], [yt2], [zt2], marker='o', color='orange', markersize=8)
    line3, = ax.plot([xt3], [yt3], [zt3], marker='o', color='red', markersize=8)
    line4, = ax.plot([xt4], [yt4], [zt4], marker='o', color='blue', markersize=8)
    line5, = ax.plot([xt5], [yt5], [zt5], marker='o', color='orange', markersize=8)
    line6, = ax.plot([xt6], [yt6], [zt6], marker='o', color='red', markersize=8)
    line7, = ax.plot([xt7], [yt7], [zt7], marker='o', color='blue', markersize=8)
    line8, = ax.plot([xt8], [yt8], [zt8], marker='o', color='orange', markersize=8)
    line9, = ax.plot([xt9], [yt9], [zt9], marker='o', color='red', markersize=8)
    # line2, = ax.plot([xt2], [yt2], [zt2], marker='o', color='orange', markersize=4)
    # line3, = ax.plot(xt21, yt21, zt21, color='purple')
    return line1, line2, line3, line4, line5, line6, line7, line8, line9
    # return line1
    # return line1, line2, line3


def data_gen():
    # global x0,y0,z0,ti, t_drang, t_range, omega1, omega2, phi
    global x0, y0, z0, x1, y1, z1, t_dlen

    # while true:
    data = []
    for ti in range(1, 3 * t_dlen):
        if ti < t_dlen:
            xt1 = x0
            xt2 = x_2
            xt3 = x_3
            xt4 = x_4
            xt5 = x_5
            xt6 = x_6
            xt7 = x_7
            xt8 = x_8
            xt9 = x_9
            yt1 = y0
            yt2 = y_2
            yt3 = y_3
            yt4 = y_4
            yt5 = y_5
            yt6 = y_6
            yt7 = y_7
            yt8 = y_8
            yt9 = y_9
            zt1 = z0 - ti
            zt2 = z_2 - ti
            zt3 = z_3 - ti
            zt4 = z_4 - ti
            zt5 = z_5 - ti
            zt6 = z_6 - ti
            zt7 = z_7 - ti
            zt8 = z_8 - ti
            zt9 = z_9 - ti
        elif ti < 2 * t_dlen:
            xt1 = x0 + ti - t_dlen
            xt2 = x_2 + ti - t_dlen
            xt3 = x_3 + ti - t_dlen
            xt4 = x_4 + ti - t_dlen
            xt5 = x_5 + ti - t_dlen
            xt6 = x_6 + ti - t_dlen
            xt7 = x_7 + ti - t_dlen
            xt8 = x_8 + ti - t_dlen
            xt9 = x_9 + ti - t_dlen
            yt1 = y0
            yt2 = y_2
            yt3 = y_3
            yt4 = y_4
            yt5 = y_5
            yt6 = y_6
            yt7 = y_7
            yt8 = y_8
            yt9 = y_9
            zt1 = zt1+1
            zt2 = zt2+2
            zt3 = zt3+4
            zt4 = zt4
            zt5 = zt5+5
            zt6 = zt6
            zt7 = zt7
            zt8 = zt8
            zt9 = zt9
        else:
            xt1 = xt1
            xt2 = xt2
            xt3 = xt3
            xt4 = xt4
            xt5 = xt5
            xt6 = xt6
            xt7 = xt7
            xt8 = xt8
            xt9 = xt9
            yt1 = y0
            yt2 = y_2
            zt1 = zt1 + (ti - 2 * t_dlen) / 2
            zt2 = zt2 + (ti - 2 * t_dlen) / 3
            zt3 = zt2 + (ti - 2 * t_dlen) /4
            zt4 = zt2 + (ti - 2 * t_dlen) /5
            zt5 = zt2 + (ti - 2 * t_dlen) /6
            zt6 = zt2 + (ti - 2 * t_dlen) /7
            zt7 = zt2 + (ti - 2 * t_dlen) /8
            zt8 = zt2 + (ti - 2 * t_dlen) /9
            zt9 = zt2 + (ti - 2 * t_dlen) / 10
        # yt2 = yt1 + r2 * np.cos(omega2 * t) / (np.cos(phi) * (1 + np.tan(phi) ** 2))
        # zt2 = zt1 + (yt2 - yt1) * np.tan(phi)
        # xt21 = xt1 + r2 * np.sin(2 * np.pi * t_range)
        # yt21 = yt1 + r2 * np.cos(2 * np.pi * t_range) / (np.cos(phi) * (1 + np.tan(phi) ** 2))
        # zt21 = zt1 + (yt21 - yt1) * np.tan(phi)
        # data.append([xt1, yt1, zt1, xt2, yt2, zt2, xt21, yt21, zt21])
        # data.append([xt1, yt1, zt1])
        data.append(
            [xt1, yt1, zt1, xt2, yt2, zt2, xt3, yt3, zt3, xt4, yt4, zt4, xt5, yt5, zt5, xt6, yt6, zt6, xt7, yt7, zt7,
             xt8, yt8, zt8, xt9, yt9, zt9])
    return data
    # yield (xt1, yt1, zt1, xt2, yt2, zt2, xt21, yt21, zt21)


if __name__ == '__main__':
    t_range = np.arange(0, 1 + 0.005, 0.005)
    t_drange = np.arange(0, 1, 0.1)
    t_len = len(t_range)
    t_dlen = len(t_drange)
    # sun's coordination
    x0 = 0
    y0 = 0
    z0 = 15
    x_2 = 3
    x_3 = 6
    x_4 = 9
    x_5 = 12
    x_6 = 15
    x_7 = 18
    x_8 = 21
    x_9 = 24
    y_2 = 0
    y_3 = 0
    y_4 = 0
    y_5 = 0
    y_6 = 0
    y_7 = 0
    y_8 = 0
    y_9 = 0
    z_2 = 15
    z_3 = 15
    z_4 = 15
    z_5 = 15
    z_6 = 15
    z_7 = 15
    z_8 = 15
    z_9 = 15

    # earth's orbit
    # x1 = x0 + r1 * np.cos(omega1 * t_range)
    # y1 = y0 + r1 * np.sin(omega1 * t_range)
    # z1 = z0 + np.zeros(t_len)
    #
    # # moon's orbit
    # x2 = x1 + r2 * np.sin(omega2 * t_range)
    # y2 = y1 + r2 * np.cos(omega2 * t_range) / (np.cos(phi) * (1 + np.tan(phi) ** 2))
    # z2 = z1 + (y2 - y1) * np.tan(phi)

    f = plt.figure(figsize=(6, 6))
    ax = f.add_subplot(111, projection='3d')
    # plt.rcParams['animation.ffmpeg_path'] = r"C:\Program Files\ffmpeg\bin\ffmpeg"
    # plt.rcParams['animation.convert_path'] = r"C:\Program Files\ImageMagick-7.0.7-Q16\magick.exe"
    ax.set_aspect('equal')
    ax.set_title("Sun-Earth-Moon Model")

    # ax.plot([0], [0], [0], marker='o', color='red', markersize=16)
    # ax.plot(x1, y1, z1, 'r')
    # ax.plot(x2, y2, z2, 'b')
    ax.set_xlim([0, 22])
    ax.set_ylim([0, 22])
    ax.set_zlim([0, 22])
    # line1 update Earth's track  dynamically
    # line2 update Moon's track dynamically
    # line3 update Moon's orbit to earth
    # line1, = ax.plot([], [], [], marker='o', color='blue', markersize=8, animated=True)
    # line2, = ax.plot([], [], [], marker='o', color='orange', markersize=4, animated=True)
    # line3, = ax.plot([], [], [], color='purple', animated=True)

    # red sphere for Sun, blue sphere for Earth, orange sphere for Moon
    ani = animmation.FuncAnimation(f, update, frames=data_gen(), init_func=init, interval=200)
    # ffwriter = animmation.ffmpegwriter(fps = 200)
    # ani.save('planet.gif', writer='imagemagick', fps=40)
    # ani.save('planet.gif', writer = ffwriter)
    plt.show()
