from manimlib import *

class VerticalBraceWithDots(Scene):
    def construct(self):
        # 创建两个 Dot 对象
        dot1 = Dot(color=BLUE)
        dot2 = Dot(color=RED)

        # 将两个对象垂直排列
        group = VGroup(dot1, dot2).arrange(DOWN, buff=1)

        # 创建一个竖向的大括号，包围两个 Dot 对象
        brace = Brace(group, LEFT)

        # 添加标签
        brace_text = brace.get_text("大括号")

        # 将对象添加到场景中
        self.play(ShowCreation(dot1))
        self.play(ShowCreation(dot2))
        self.play(ShowCreation(brace))
        self.play(Write(brace_text))

        self.wait(2)