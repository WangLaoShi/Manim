from manimlib import *


class PositioningExample(Scene):
    def construct(self):
        # 创建三个不同的对象
        circle = Circle().set_fill(BLUE, opacity=0.5)
        square = Square().set_fill(RED, opacity=0.5)
        triangle = Triangle().set_fill(GREEN, opacity=0.5)

        # 将对象放置在场景的不同位置
        circle.move_to(LEFT * 3 + UP * 2)  # 将圆形移动到左上方
        square.move_to(RIGHT * 3 + UP * 2)  # 将正方形移动到右上方
        triangle.move_to(DOWN * 2)  # 将三角形移动到下方中央

        # 显示对象
        self.play(ShowCreation(circle))
        self.play(ShowCreation(square))
        self.play(ShowCreation(triangle))

        self.wait(2)

        # 使用 shift 方法移动对象
        self.play(circle.animate.shift(DOWN * 2))  # 将圆形向下移动
        self.play(square.animate.shift(LEFT * 2))  # 将正方形向左移动
        self.play(triangle.animate.shift(UP * 2 + RIGHT * 3))  # 将三角形向上和向右移动

        self.wait(2)

        # 使用 align_to 方法对齐对象
        self.play(circle.animate.align_to(square, UP))  # 将圆形的顶部与正方形对齐
        self.play(triangle.animate.align_to(square, LEFT))  # 将三角形的左边与正方形对齐

        self.wait(2)