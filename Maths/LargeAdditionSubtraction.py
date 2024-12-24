from manimlib import *


class LargeAdditionSubtraction(Scene):
    def create_rectangles(self, num, color):
        rects = VGroup(*[Square(side_length=0.3) for _ in range(num)]).arrange_in_grid(n_rows=10, buff=0.1)
        rects.set_fill(color, opacity=0.5)
        return rects

    def construct(self):
        # 定义两个较大数字
        num1 = 75
        num2 = 25

        # 创建表示两个数字的矩形框
        rects_one = self.create_rectangles(num1, BLUE)
        rects_two = self.create_rectangles(num2, RED)

        # 创建加号、减号和等号
        plus = Text("+")
        minus = Text("-")
        equals = Text("=")

        # 创建结果的矩形框
        result_addition = self.create_rectangles(num1 + num2, GREEN)
        result_subtraction = self.create_rectangles(num1 - num2, YELLOW)

        # 定位各个对象
        rects_one.move_to(LEFT * 5 + UP * 2)
        plus.next_to(rects_one, RIGHT, buff=0.5)
        rects_two.next_to(plus, RIGHT, buff=0.5)
        equals.next_to(rects_two, RIGHT, buff=0.5)
        result_addition.next_to(equals, RIGHT, buff=0.5)

        # 显示加法矩形框和符号
        self.play(ShowCreation(rects_one))
        self.play(ShowCreation(rects_two))
        self.play(Write(plus))
        self.play(Write(equals))

        # 合并矩形框并显示加法结果
        self.play(rects_one.animate.shift(RIGHT * 2 + DOWN * 2))
        self.play(rects_two.animate.shift(LEFT * 2 + DOWN * 2))
        self.play(ShowCreation(result_addition))

        self.wait(2)

        # 定位减法对象
        minus.move_to(plus.get_center())
        result_subtraction.next_to(equals, RIGHT, buff=0.5).shift(DOWN * 2)

        # 移除加法对象
        self.play(FadeOut(result_addition))
        self.play(FadeOut(rects_one))
        self.play(FadeOut(rects_two))

        # 显示减法矩形框和符号
        rects_one.move_to(LEFT * 5 + UP * 2)
        self.play(ShowCreation(rects_one))
        self.play(ShowCreation(rects_two))
        self.play(Write(minus))
        self.play(Write(equals))

        # 移除矩形框并显示减法结果
        self.play(rects_two.animate.shift(DOWN * 2 + LEFT * 5))
        self.play(FadeOut(rects_two))
        self.play(ShowCreation(result_subtraction))

        self.wait(2)

