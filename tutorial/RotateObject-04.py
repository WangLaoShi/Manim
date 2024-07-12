from manimlib import *
class RotateObject(Scene):
    def construct(self):
        textM = Text("Text")
        textC = Text("Reference text")
        textM.rotate(PI/4, textC)
        self.play(Write(textM), Write(textC))
        self.wait(2)