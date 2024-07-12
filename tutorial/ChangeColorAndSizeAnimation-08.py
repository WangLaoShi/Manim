from manimlib import *
class ChangeColorAndSizeAnimation(Scene):
    def construct(self):
        text = TexText("Text")
        self.play(Write(text))

        text.generate_target()
        text.target = TexText("Target")
        text.target.set_color(RED)
        text.target.scale(2)
        text.target.shift(LEFT)

        self.play(MoveToTarget(text), run_time=2)
        self.wait()