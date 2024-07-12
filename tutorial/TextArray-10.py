from manimlib import *
class TextArray(Scene):
    def construct(self):
        dot1 = Dot()
        dot1.scale(3)
        dot1.shift(UP)
        dot2 = Dot()
        self.add(dot1, dot2)
        self.wait(3)