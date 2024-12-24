from manimlib import *


class AdditionScene(Scene):
    def construct(self):
        # 创建数字1和2的Mobject
        one = Text("1").shift(LEFT)
        two = Text("2").shift(RIGHT)

        # 创建加号和等号
        plus = Text("+")
        equals = Text("=")

        # 创建结果数字3的Mobject
        result = Text("3")

        # 将所有Mobjects放在场景中
        self.play(Write(one))
        self.play(Write(plus.next_to(one, RIGHT)))
        self.play(Write(two.next_to(plus, RIGHT)))
        self.play(Write(equals.next_to(two, RIGHT)))

        # 显示结果
        self.play(Write(result.next_to(equals, RIGHT)))

        # 添加一些动画效果
        self.play(one.animate.shift(UP))
        self.play(two.animate.shift(UP))
        self.play(result.animate.scale(1.5).set_color(YELLOW))

        self.wait(2)
