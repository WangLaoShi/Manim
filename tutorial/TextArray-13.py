from manimlib import *
class TexArray(Scene):
    def construct(self):
        text = TexText("A", "$\\frac{B}{C}$", "D", "E")
        text[0].set_color(RED)
        text[1].set_color(ORANGE)
        text[2].set_color(YELLOW)
        text[3].set_color(GREEN)
        self.play(Write(text))
        self.wait(2)