from manimlib import *
class RotateObject(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Reference text")

        self.play(Write(textM), Write(textC))
        textM.shift(UP)
        self.wait(2)
        textM.rotate(PI / 4)
        self.wait(2)
