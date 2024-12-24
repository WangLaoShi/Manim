from manimlib import *


class LargeAddition(Scene):
    def create_rectangles(self, num, color):
        rects = VGroup(*[Square(side_length=0.5) for _ in range(num)]).arrange(RIGHT, buff=0.1)
        rects.set_fill(color, opacity=0.5)
        if num > 4:
            rects.rotate(PI/2)
        return rects

    def addition(self,num1,num2):
        # 创建表示两个数字的矩形框
        rects_one = self.create_rectangles(num1, BLUE)
        rects_two = self.create_rectangles(num2, RED)

        # 创建加号和等号
        plus = Text("+")
        equals = Text("=")

        # 创建结果的矩形框
        result_num = num1 + num2
        result_rects = self.create_rectangles(result_num, GREEN)

        # 定位各个对象
        rects_one.move_to(LEFT * 3)
        plus.next_to(rects_one, RIGHT, buff=0.5)
        rects_two.next_to(plus, RIGHT, buff=0.5)
        equals.next_to(rects_two, RIGHT, buff=0.5)
        result_rects.next_to(equals, RIGHT, buff=0.5)

        # 显示矩形框和符号
        self.play(ShowCreation(rects_one))
        self.play(ShowCreation(rects_two))
        self.play(Write(plus))
        self.play(Write(equals))

        # 合并矩形框并显示结果
        self.play(rects_one.animate.shift(RIGHT * 2 + DOWN * 2))
        self.play(rects_two.animate.shift(LEFT * 2 + DOWN * 2))
        self.play(ShowCreation(result_rects))

        self.wait(2)

    def construct(self):
        # 定义两个较大数字
        num1 = 7
        num2 = 5
        self.addition(num1,num2)
