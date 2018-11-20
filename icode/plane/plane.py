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

    # 右翻
    def turn_right(self):
        self.x += 1

    # 前翻
    def turn_forward(self):
        self.y += 1

    # 后翻
    def turn_back(self):
        self.y -= 1

    # 左飞
    def to_left(self):
        self.x -= 1

    # 右飞
    def to_right(self):
        self.x += 1

    # 前飞
    def to_forward(self):
        self.y += 1

    # 后飞
    def to_back(self):
        self.y -= 1

    # 上升
    def to_upper(self):
        self.z += 1

    # 下降
    def to_down(self):
        self.z -= 1