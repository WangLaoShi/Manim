from manimlib import *
class ChangeColorAndSizeAnimation(Scene):
    def construct(self):
        text = Text("Text")
        text.scale(2)
        text.shift(LEFT * 2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.shift, RIGHT * 2,
            text.scale, 2,
            text.set_color, RED,
            run_time=20
        )
        self.wait()