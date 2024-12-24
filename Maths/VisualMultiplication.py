from manimlib import *

class VisualMultiplication(Scene):
    def construct(self):
        # 设置乘法因子
        a = 7
        b = 8

        # 创建点阵组
        dot_group = VGroup()

        # 创建点阵，表示乘法结果
        for i in range(a):
            for j in range(b):
                dot = Dot()
                dot.move_to(i * RIGHT + j * UP)
                dot_group.add(dot)

        # 将点阵居中
        dot_group.move_to(ORIGIN)

        # 显示点阵
        self.play(Write(dot_group))
        self.wait(2)

        # 添加标签
        multiplication_label = TexText(f"${a} \\times {b} = {a * b}$")
        multiplication_label.next_to(dot_group, DOWN)

        # 显示标签
        self.play(Write(multiplication_label))
        self.wait(2)