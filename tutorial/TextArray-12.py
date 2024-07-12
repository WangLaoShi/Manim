from manimlib import *
class TextArray(Scene):
    def construct(self):
        text = TexText("A", "B", "C", "D", "E", "F")
        text[0].set_color(RED)
        text[1].set_color(ORANGE)
        text[2].set_color(YELLOW)
        text[3].set_color(GREEN)
        text[4].set_color(BLUE) # Hexadecimal color
        self.play(Write(text))
        self.wait(2)