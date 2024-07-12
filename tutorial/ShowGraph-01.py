from manimlib import *
class ShowGraph(Scene):
    def construct(self):
        print("dot = Dot()")
        dot = Dot()
        self.wait(20)

        print("dot.to_edge(UL)")
        dot.to_edge(UL)
        self.play(FadeIn(dot))
        self.wait(20)

        print("text = TextMobject(\"text\")")
        text = Text("text")
        self.wait(20)

        print("text.to_corner(UP)")
        text.to_corner(UP)
        self.play(Write(text))
        self.wait(20)