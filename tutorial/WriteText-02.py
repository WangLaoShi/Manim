from manimlib import *

class WriteText(Scene):
    def construct(self):
        seconds = 3
        text = Text("A Text")
        self.play(Write(text), run_time=seconds)
        text.to_edge(UP)
        text.move_to(1 * UP + 0.1 * RIGHT)
        self.wait(seconds)
        # self.play(Write(text), run_time=seconds)
        self.wait(seconds)
        # self.remove(text)
        self.embed()