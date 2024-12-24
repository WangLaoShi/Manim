from manimlib import *


class AdditionWithRectangles(Scene):

    def additon(self,add1,add2):
        ## 1 + 2 = 3 的例子

        # 创建表示数字1的矩形框
        rects_one = VGroup(*[Square(side_length=1) for _ in range(add1)]).arrange(RIGHT, buff=0.1)
        rects_one.set_fill(BLUE, opacity=0.5)
        rects_one.move_to(LEFT * 3)

        brace1 = Brace(rects_one, UP)
        label1 = Text(str(add1))
        label1.next_to(brace1, UP)

        # 创建表示数字2的矩形框
        rects_two = VGroup(*[Square(side_length=1) for _ in range(add2)]).arrange(RIGHT, buff=0.1)
        rects_two.set_fill(RED, opacity=0.5)
        rects_two.move_to(RIGHT * 1)

        brace2 = Brace(rects_two, UP)
        label2 = Text(str(add2))
        label2.next_to(brace2, UP)

        # 创建加号和等号
        plus = Text("+").move_to(LEFT * 1)
        equals = Text("=").move_to(RIGHT * 3)
        question = Text("?").move_to(RIGHT * 5)

        # 创建结果的矩形框
        result_rects = VGroup(*[Square(side_length=1) for _ in range(add1+add2)]).arrange(RIGHT, buff=0.1)
        result_rects[0:add1].set_fill(BLUE, opacity=0.5)
        result_rects[add1:].set_fill(RED, opacity=0.5)
        result_rects.move_to(DOWN * 2)

        brace3 = Brace(result_rects, BOTTOM)
        label3 = Text(str(add1+add2))
        label3.next_to(brace3, DOWN)

        # 显示矩形框和符号
        self.play(ShowCreation(rects_one))
        self.play(ShowCreation(brace1))
        self.play(ShowCreation(label1))
        self.play(ShowCreation(rects_two))
        self.play(ShowCreation(brace2))
        self.play(ShowCreation(label2))
        self.play(Write(plus))
        self.play(Write(equals))
        self.play(Write(question))

        # 合并矩形框并显示结果
        # self.play(rects_one.animate.shift(RIGHT * 2 + DOWN * 2))
        # self.play(rects_two.animate.shift(LEFT * 2 + DOWN * 2))
        self.play(ShowCreation(result_rects))
        self.play(ShowCreation(brace3))
        self.play(ShowCreation(label3))
        self.wait(5)

        self.remove(question)

        question3 = Text(str(add1+add2))
        question3.next_to(equals, RIGHT * 5)
        question3.scale(2)
        question3.set_color(RED)
        self.play(ShowCreation(question3))
        self.wait(2)

        ## 1 + 2 = 3 的例子
    def construct(self):
        self.additon(1,2)
        self.clear()
        self.additon(2, 3)
        self.clear()
        self.additon(4, 6)

