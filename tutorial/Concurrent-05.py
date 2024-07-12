from manimlib import *
class Concurrent(Scene):
    def construct(self):
        dot1 = Dot()

        dot2 = Dot()
        dot2.shift(UP)

        dot3 = Dot()
        dot3.shift(DOWN)

        # 单个动画的演示
        self.play(Write(dot1))
        # 故意使用 i,j 是为了显示 zip 的使用
        for i, j in zip([dot1, dot1], [dot2, dot3]):
            # 多个动画演示
            self.play( *[Transform(i.copy(), j)])
            self.wait()